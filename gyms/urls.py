from django.urls import path

from . import views

app_name = 'gyms'
urlpatterns = [
    path('', views.index, name='index'),
    path('gym/<int:gym_id>', views.gym_detail, name='gym_detail'),
    path('trainer/<int:trainer_id>', views.trainer_detail, name='trainer_detail'),
    path('add_abonement/', views.add_abonement, name='add_abonement'),
    path('delete_abonement/', views.delete_abonement, name='delete_abonement'),
    path('register/', views.register, name='register'),
    path('personal_account/', views.information_of_user, name='information_of_user'),
    path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile'),
]