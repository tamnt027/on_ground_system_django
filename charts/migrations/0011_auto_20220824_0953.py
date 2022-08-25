# Generated by Django 3.2 on 2022-08-24 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0010_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 9, 53, 35, 347156)),
        ),
        migrations.AddField(
            model_name='chart',
            name='display_priority',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]