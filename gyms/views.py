from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Gym, Trainer, Abonement
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserForm, NewUserForm




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
    return redirect('gyms:gym_detail', request.POST['gym_id'])

def delete_abonement(request):
    gym = get_object_or_404(Gym, id=request.POST['gym_id'])
    abonement = Abonement.objects.filter(gym=gym, profile=request.user.profile)
    abonement.delete()
    request.user.profile.save()
    return redirect('gyms:gym_detail', request.POST['gym_id'])

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы зарегестрировались успешно.")
            return redirect('gyms:index')
    else:
        messages.error(request, "Нормально регайся!")
        form = NewUserForm()
        return render(request, "registration/register.html", context={"form": form})


@login_required
def information_of_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    abonement = Abonement.objects.filter(profile=request.user.profile)
    return render(request, 'gyms/profile.html', {'user': user, 'abonement':abonement})


@login_required
def edit_profile(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = get_object_or_404(User, id=user_id)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('gyms:profile', user.id)
    else:
        form = UserForm(instance=request.user)
    return render(request, 'gyms/edit_profile.html', {'form': form})