# Generated by Django 3.2 on 2022-08-24 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0007_auto_20220823_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesdisplay',
            name='measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='displayes', to='charts.lorameasurement'),
        ),
    ]
