from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Gym, Trainer

def index(request):
    return render(request, 'gyms/index.html', {'title': 'Тренажерки', 'gyms': Gym.objects.all()})
