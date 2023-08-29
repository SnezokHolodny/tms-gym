from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Gym, Trainer

def index(request):
    return render(request, 'gyms/index.html', {'title': 'Тренажерки', 'gyms': Gym.objects.all()})


def gym_detail(request, gym_id: int):
    return render(request, 'gyms/gym_detail.html', {
        'gym': get_object_or_404(Gym, id=gym_id),
    })

def trainer_detail(request, trainer_id: int):
    return render(request, 'gyms/trainer_detail.html', {
        'trainer': get_object_or_404(Trainer, id=trainer_id),
    })

@login_required
def add_abonement(request: HttpRequest):
    profile = request.user.profile
    assert request.method == 'POST'
    trainer_id = request.POST['trainer_id']
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return redirect(request, 'gyms/trainer_detail', trainer)

