from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Gym, Trainer, Abonement

def index(request):
    return render(request, 'gyms/index.html', {'title': 'Тренажерки', 'gyms': Gym.objects.all()})


def gym_detail(request, gym_id: int):
    info = Abonement.objects.filter(profile=request.user.profile, gym__id=gym_id)
    if info:
        cheack_element = False
    else:
        cheack_element = True
    return render(request, 'gyms/gym_detail.html', {
        'gym': get_object_or_404(Gym, id=gym_id), 'cheack_element': cheack_element
    })

def trainer_detail(request, trainer_id: int):
    return render(request, 'gyms/trainer_detail.html', {
        'trainer': get_object_or_404(Trainer, id=trainer_id),
    })

@login_required
def add_abonement(request: HttpRequest):
    gym = get_object_or_404(Gym, id=request.POST['gym_id'])
    trainer = get_object_or_404(Trainer, id=request.POST['trainer_id'])
    profile = request.user.profile
    abonement = Abonement.objects.create(gym=gym, trainer=trainer, profile=profile, time=request.POST['time'])
    return redirect('gyms:gym', request.POST['gym_id'])

def delete_abonement(request):
    gym = get_object_or_404(Gym, id=request.POST['gym_id'])
    abonement = get_object_or_404(Abonement, gym__id=request.POST['gym_id'], profile=request.user.profile)
    abonement.delete()
    request.user.profile.save()
    return redirect('gyms:gym', request.POST['gym_id'])


