from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("homescreen.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})
def scatterplot(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("scatterplot.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})

def radialboxplot(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("radialboxplot.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})

def streamgraph(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("streamgraph.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})

def linegraph(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("linegraph.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})
def overview(request):
	# print request
	# return HttpResponse("Hello World!")
	return render_to_response("overview.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})