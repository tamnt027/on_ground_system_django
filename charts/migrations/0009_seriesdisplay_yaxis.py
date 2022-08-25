# Generated by Django 3.2 on 2022-08-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0008_seriesdisplay_measurement'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesdisplay',
            name='yaxis',
            field=models.CharField(choices=[('y1', 'Yaxisl1'), ('y2', 'Yaxisr1'), ('y3', 'Yaxisl2'), ('y4', 'Yaxisr2')], default='y1', max_length=10),
        ),
    ]
