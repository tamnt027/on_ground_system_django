# Generated by Django 3.2 on 2022-08-25 03:12

import colorfield.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0017_alter_chart_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='color',
            field=colorfield.fields.ColorField(default='#000000', help_text='Title color', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='chart',
            name='font_size',
            field=models.IntegerField(default=20, help_text='Title font size'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 3, 12, 56, 301872, tzinfo=utc), editable=False),
        ),
    ]
