from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, Brat! Na sportike ter?')
