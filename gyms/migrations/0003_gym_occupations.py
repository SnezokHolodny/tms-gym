# Generated by Django 4.2.3 on 2023-08-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0002_trainer_gym'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='occupations',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
