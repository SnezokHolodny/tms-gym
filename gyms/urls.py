from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.index, name='index'),
    path('gym/<int:gym_id>', views.gym_detail, name='gym_detail'),
    path('trainer/<int:trainer_id>', views.trainer_detail, name='trainer_detail'),
]