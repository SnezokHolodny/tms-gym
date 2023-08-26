from django.db import models
from django.contrib.auth.models import User


class Gym(models.Model):
    name = models.CharField(max_length=200)
    time_work = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)



    def __str__(self):
        return self.name



class Trainer(models.Model):
    name = models.CharField(max_length=200)
    year_old = models.IntegerField(default=0)
    time_work = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, null=True, related_name='trainers')


    def __str__(self):
        return self.name


class Abonement(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE,
                                related_name='abonements')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE,
                                related_name='abonements')
    profile = models.ForeignKey(Gym, on_delete=models.CASCADE,
                                related_name='abonements')


class PriceAbonement(models.Model):
    price = models.IntegerField(default=0)
    abonement = models.ForeignKey(Abonement, on_delete=models.CASCADE,
                                          null=True, blank=True, related_name='price')


class NameAbonement(models.Model):
    name = models.CharField(max_length=100)
    abonement = models.ForeignKey(Abonement, on_delete=models.CASCADE,
                                          null=True, blank=True, related_name='name')


class TimeAbonement(models.Model):
    time = models.CharField(max_length=100)
    abonement = models.ForeignKey(Abonement, on_delete=models.CASCADE,
                                          null=True, blank=True, related_name='time_abonement')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



