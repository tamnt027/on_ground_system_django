# Generated by Django 3.2 on 2022-08-24 03:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0012_alter_chart_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 24, 3, 0, 40, 667461, tzinfo=utc), editable=False),
        ),
    ]
