from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.index, name='index'),
    path('gyms/<int:gym_id', views.gym_detail, name='gym_detail'),
]