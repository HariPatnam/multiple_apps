from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app_2nd1(request):
    return HttpResponse('this is app2 function')

def app_2nd(request):
    return HttpResponse('this is app_2nd function')
