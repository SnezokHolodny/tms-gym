# Generated by Django 4.2.3 on 2023-08-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0004_abonement_remove_gym_occupations_timeabonement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priceabonement',
            name='abonement',
        ),
        migrations.RemoveField(
            model_name='timeabonement',
            name='abonement',
        ),
        migrations.AddField(
            model_name='abonement',
            name='time',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.DeleteModel(
            name='NameAbonement',
        ),
        migrations.DeleteModel(
            name='PriceAbonement',
        ),
        migrations.DeleteModel(
            name='TimeAbonement',
        ),
    ]
