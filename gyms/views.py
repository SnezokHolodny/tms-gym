from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Gym, Trainer

def index(request):
    return render(request, 'gyms/index.html', {'title': 'Тренажерки', 'gyms': Gym.objects.all()})


def gym_detail(request, gym_id: int):
    return render(request, 'gyms/gym_detail.html', {
        'gym': get_object_or_404(Gym, id=gym_id),
    })
