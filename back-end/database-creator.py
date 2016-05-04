import os
import time
import json
import csv
import pandas as pd
from pandas import Timestamp
from datetime import datetime
import vis as selfspyVis
from dateutil.parser import parse
import sys
reload(sys);
sys.setdefaultencoding("utf8")


pathToDatabase = "/Users/lukemcgartland/Google Drive/Academy/Year 2/Spring/Information Visualization/Final Project/database/"
pathToRawData = "/Users/lukemcgartland/Google Drive/Academy/Year 2/Spring/Information Visualization/Final Project/raw-data/"
#sampleDay = "{\"day\":{\"date\":\"\",\"steps\":\"\",\"exercise\":\"\",\"sleep\":\"\",\"weight\":\"\"}\"}"

def createDateFile(date):
	path = pathToDatabase + monthFromDate(date) +"/"+date+".txt"
	data = {'date': date}
	writeDayToFile(data, path)
	#touch(path)
	return

def monthFromDate(date):
	return str(date)[:7]
	
# def touch(path):
#     with open(path, 'a'):
#         os.utime(path, None)

def createMonthFolder(month):
	directory = pathToDatabase + month
	if not os.path.exists(directory):
		print "not there"
		os.makedirs(directory)
	return
    
def writeDayToFile(data, path):
	with open(path, 'w') as outfile:
		json.dump(data, outfile)

def appendDataToDate(date, key, data):
	path = pathToDatabase + monthFromDate(date) +"/"+date+".txt"
	with open(path) as json_file:
		json_data = json.load(json_file)
		json_data[key]=data
		writeDayToFile(json_data, path)

#CSV
def importListFromCSV(path):
	with open(path, 'rb') as f:
		reader = csv.reader(f)
		your_list = list(reader)
		return your_list

#SetupFunctions

#Run this one first to generate DB
def setUpFileStructure():
	dateList = pd.date_range('1/1/2016', pd.datetime.today()).tolist()
	newDateList = [str(date)[:10] for date in dateList]
	monthList = pd.date_range((Timestamp('20161231') +pd.DateOffset(months=-12)), periods=12, freq='MS').tolist()
	newMonthList = [str(month)[:7] for month in monthList]
	for month in newMonthList:
		createMonthFolder(month)
	for date in newDateList:
		createDateFile(date)

def createTotalDateList():
	dateList = pd.date_range('1/1/2016', pd.datetime.today()).tolist()
	newDateList = [str(date)[:10] for date in dateList]
	return newDateList


def setUpWeights():
	txt = open(pathToRawData+"weight/weight.txt").read()
	weights = txt.split("\n");
	#print weights
	for entry in weights:
		if (entry !=""):
			date = str(entry)[:10]
			dateParts = date.split(".")
			date = dateParts[0] +"-"+ dateParts[1] +"-"+ dateParts[2]
			weight = entry.split(" ")
			weight = weight[1]
			appendDataToDate(date, "weight", weight)
			#print date + " " + weight

def setUpMSBand():
	input_dir = pathToRawData +"microsoft-band/" #or any other path
	files = os.listdir(input_dir) #listdir will give the file names
	files_of_interest = (f for f in files if "Daily_Summary" in f)
	for f in files_of_interest:
		full_name = os.path.join(input_dir, f)
		msbandList =  importListFromCSV(full_name)
		msbandReferenceList = msbandList.pop(0)
		#now lets add some data from the csv to our json file database
		for msbandEntry in msbandList:
			date = msbandEntry[0]
			steps = msbandEntry[1]
			appendDataToDate(date, "Steps", steps)

			calories = msbandEntry[2]
			appendDataToDate(date, "Calories", calories)

			miles = msbandEntry[6]
			appendDataToDate(date, "Miles", miles)

			secondsSlept = msbandEntry[14]
			appendDataToDate(date, "Sleep", secondsSlept)

			gym = msbandEntry[24]
			if (gym == ''):
				gym = 0
			else:
				gym = int(gym)

			guidedWorkout = msbandEntry[27]
			if (guidedWorkout == ''):
				guidedWorkout = 0
			else:
				guidedWorkout = int(guidedWorkout)

			secondsExercise = gym + guidedWorkout
			appendDataToDate(date, "Exercise", secondsExercise)

def setUpSelfSpy():
	#selfspy times are in seconds!!!!
	ss = selfspyVis.main()
	dateList = createTotalDateList()
	for date in dateList:
		#print date
		ssDict = selfSpyGetDate(ss, date)
		for key, elem in ssDict.items():
			appendDataToDate(date, key, elem)

	
	#print ss.args
def setUpSelfSpyTitle():
	ss = selfspyVis.main()
	dateList = createTotalDateList()
	for date in dateList:
		#print date
		ssDict = selfSpyGetTitleDate(ss, date)

		instagram = 0
		twitter = 0
		for key, elem in ssDict.items():
			#appendDataToDate(date, key, elem)
			k = str(key)
			e = str(elem)
			
			if (k.find("Instagram") != -1):
				instagram = instagram + int(e)
			if (k.find("Twitter") != -1):
				twitter = twitter + int(e)
		
		if instagram != 0:
			appendDataToDate(date, "Instagram", instagram)
		if twitter != 0:
			appendDataToDate(date, "Twitter", twitter)

def selfSpyGetTitleDate(ss, date):
	#date is in yyyy-mm-dd form
	#convert date to proper format
	parts = date.split("-");

	year = parts[0]
	month = parts[1]
	day = parts[2]

	ss.args["tactive"]=1
	ss.args["limit"] = ["1", "days"]
	ss.args["date"] = [year, month, day]
	return ss.do()

def selfSpyGetDate(ss, date):
	#date is in yyyy-mm-dd form
	#convert date to proper format
	parts = date.split("-");

	year = parts[0]
	month = parts[1]
	day = parts[2]

	ss.args["pactive"]=1
	ss.args["limit"] = ["1", "days"]
	ss.args["date"] = [year, month, day]
	return ss.do()

def setUpLastFM():
	input_dir = pathToRawData +"lastfm/" #or any other path
	files = os.listdir(input_dir) #listdir will give the file names
	files_of_interest = (f for f in files if "Lastfm" in f)
	for f in files_of_interest:
		full_name = os.path.join(input_dir, f)
		lastFMlist =  importListFromCSV(full_name)
		parsedList = []
		for song in lastFMlist:
			parsedDate = parse(song[3])
			parsedList.append(parsedDate.strftime('%Y-%m-%d')) 
		from collections import Counter
		c=Counter(parsedList)
		values = c.values()
		keys = c.keys()
		for i in range(len(keys)):
			print keys[i] + " " + str(values[i])
			appendDataToDate(keys[i], "Songs", values[i])

def main(): 
	setUpFileStructure()
	setUpWeights()
	setUpMSBand()
	setUpSelfSpy()
	setUpSelfSpyTitle()
	setUpLastFM()
	

if __name__ == '__main__':
    main()

#{'key_freqs': False, 'process': None, 'back': None, 'date': ['2016', '01', '01'], 'periods': None, 'showtext': False, 'id': None, 'password': u'iamironman', 'data_dir': '/Users/lukemcgartland/.selfspy', 'clock': None, 'config': None, 'clicks': False, 'body': None, 'human_readable': False, 'pactive': 180, 'tactive': None, 'ratios': None, 'active': None, 'min_keys': None, 'tkeys': False, 'title': None, 'limit': ['1', 'days'], 'pkeys': False}