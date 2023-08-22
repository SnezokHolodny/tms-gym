from django.contrib import admin
from .models import Gym, Trainer

admin.site.register(Gym)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_old', 'time_work']
    list_filter = ['name', 'year_old']
    search_fields = ['name', 'year_old']


