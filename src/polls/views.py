from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world! You're in polls app home page!")