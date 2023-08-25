from django.contrib import admin
from .models import Gym, Trainer





@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'year_old', 'time_work']}),
        ('name', {'fields': ['gym']}),
    ]
    list_display = ['name', 'year_old', 'time_work']
    list_filter = ['name', 'year_old']
    search_fields = ['name', 'year_old']


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_work', 'adress']
    list_filter = ['name']
    search_fields = ['name']



