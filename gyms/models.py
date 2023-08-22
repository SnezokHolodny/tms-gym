from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    time_work = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Trainer(models.Model):
    name = models.CharField(max_length=200)
    year_old = models.IntegerField(default=0)
    time_work = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='trainers')

    def __str__(self):
        return self.name


