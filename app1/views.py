from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app_1(request):
    return HttpResponse('this is first app_1 project')

def app_2(request):
    return HttpResponse('this is first app_2 project')
