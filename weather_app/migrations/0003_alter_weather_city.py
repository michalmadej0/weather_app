# Generated by Django 4.1.5 on 2023-01-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0002_rename_temperature_weather_temp_weather_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='city',
            field=models.CharField(default='city', max_length=64),
        ),
    ]