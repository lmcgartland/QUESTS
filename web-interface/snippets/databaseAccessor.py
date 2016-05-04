from django.http import HttpResponse
import json
import pandas as pd
from pandas import Timestamp
from datetime import datetime

pathToDatabase = "/Users/lukemcgartland/Google Drive/Academy/Year 2/Spring/Information Visualization/Final Project/database/"
#pathToDatabase = "/home/pi/Final Project/database/"

def monthFromDate(date):
    return str(date)[:7]
def getActivityOnDate(date, keys):
        path = pathToDatabase + monthFromDate(date) +"/"+date+".txt"
        dict = {};
        try:
            with open(path) as json_file:
                json_data = json.load(json_file)
                
                for key in keys:
                    try:
                        dict[key] = json_data[key]
                    except: 
                        dict[key] = ""
        except Exception, e:
            print e
            pass
            #no data essentially could have better solution
        return dict
            

def getDatesForPeriod(end, period):
    pass


class DatabaseAccessor():
    def __init__(self):
        pass

    
    def getInfoForRequest(unknown, request):
        end = None
        period = None
        activities = None
        week = [0, 1, 2, 3, 4, 5, 6]
        if len(request.GET.getlist('end')) > 0:
            end = request.GET.getlist('end')[0]
        if len(request.GET.getlist('period')) > 0:
            period = request.GET.getlist('period')[0]
        if len(request.GET.getlist('period')) > 0:
            activities = request.GET.getlist('activity')
        if len(request.GET.getlist('day')) > 0:
            week = request.GET.getlist('day')
        

        if end is None or period is None or activities is None:
            return "ERROR"

        periodDate = end.replace("-", "")
        period = pd.date_range((Timestamp(periodDate) +pd.DateOffset(days=int(period)*-1)), Timestamp(periodDate))

        period = period.tolist()
       
        datesFilteredByDay = []
        for day in period:
            for dayOfWeek in week:
                if day.weekday() == int(dayOfWeek):
                    datesFilteredByDay.append(day)

        newPeriod = [str(month)[:10] for month in datesFilteredByDay]

        arrayToReturn = []
        for date in newPeriod:
            arrayToReturn.append(getActivityOnDate(date, activities))

        return arrayToReturn#getActivityOnDate(end, activities[0])
        #http://127.0.0.1:8000/snippets/?end=2016-02-03&period=30&activity=iTunes&activity=Spotify
        
