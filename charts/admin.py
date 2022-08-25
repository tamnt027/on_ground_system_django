from django.contrib import admin
from .models import Chart, SeriesDisplay, LoraMeasurement
# Register your models here.

admin.site.register(LoraMeasurement)
admin.site.register(SeriesDisplay)
admin.site.register(Chart)