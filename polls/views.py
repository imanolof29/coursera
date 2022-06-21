from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def owner(request):
       return HttpResponse("Hello, world. 475fe344 is the polls index.")