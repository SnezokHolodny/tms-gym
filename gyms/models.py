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
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='abonements')
    time = models.CharField(max_length=100, default='-')

    def __str__(self):
        return f'{self.id} - {self.profile} - {self.trainer} - {self.gym} - {self.time}'





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



