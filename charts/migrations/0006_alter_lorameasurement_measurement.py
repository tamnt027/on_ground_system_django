# Generated by Django 3.2 on 2022-08-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_auto_20220823_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lorameasurement',
            name='measurement',
            field=models.CharField(choices=[('Measurement 01', 'temp0'), ('Measurement 02', 'temp2')], max_length=50),
        ),
    ]
