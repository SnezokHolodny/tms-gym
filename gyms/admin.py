from django.contrib import admin
from .models import Gym, Trainer, Abonement, Profile



class TrainerInline(admin.TabularInline):
    model = Trainer
    extra = 0


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
    inlines = [TrainerInline]



@admin.register(Abonement)
class AbonementAdmin(admin.ModelAdmin):
    list_display = ['trainer', 'gym', 'profile']

class AbonementInline(admin.TabularInline):
    model = Abonement
    extra = 0
    inlines = [TrainerInline]




admin.site.register(Profile)
