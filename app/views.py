from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wishing(request):
    return HttpResponse('<marquee><h2>Happy Birthday my dear Littel Prince<h2><marquee>')

def happy(request):
    return HttpResponse('<marquee>I Love You Soo Muchh my prince</marquee')

def india(request):
    return HttpResponse('<marquee><b><u>Welcome to India</marquee>')

def django(request):
    return HttpResponse('<marquee><h2>Tommrrow  Django New Batch start Time:10:30 To 12:30<h2>')