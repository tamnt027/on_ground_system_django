from pyexpat import model
from django.utils import timezone
from django.db import models
from colorfield.fields import ColorField

from .myenums import ChartMode, ChartType, YAxisType
from .influxdb_helper import InfluxDbHelper
# Create your models here.

class LoraMeasurement(models.Model):
    name = models.CharField(max_length=100, null=False)
    device_id = models.CharField(max_length=20, null=False, choices=InfluxDbHelper.get_instance().get_all_device_ids())
    measurement = models.CharField(max_length=50, null=False, choices=InfluxDbHelper.get_instance().get_all_measurements())
    port = models.IntegerField(default=1, null=False)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name}"
    

class SeriesDisplay(models.Model):
    name = models.CharField(max_length=32, null=False)
    mode = models.CharField(max_length=16, choices=ChartMode.choices, default= ChartMode.Lines)
    chart_type = models.CharField(max_length=16, choices=ChartType.choices, default= ChartType.Scatter)
    color = ColorField(default='#0000FF', format="hexa")
    yaxis = models.CharField(max_length=10, null=False, choices= YAxisType.choices, default=YAxisType.YAxisLeft )
    measurement = models.ForeignKey(LoraMeasurement, null=True, on_delete=models.CASCADE, related_name="displayes")
    
    def __str__(self):
        return f"{self.id}. {self.name}"
    
class Chart(models.Model):
    title = models.CharField(max_length=64, null=False, default="New Chart Title")
    display_priority = models.PositiveSmallIntegerField(default=0,  help_text="Smaller value has higher priority to appear")
    color = ColorField(default='#000000', format="hexa", help_text="Title color")
    font_size = models.IntegerField(default=20, null=False, help_text="Title font size")
    created_date = models.DateTimeField(default=timezone.now(), editable=False)
    active = models.BooleanField(default=True, help_text="Uncheck to prevent displaying")
    series_displays = models.ManyToManyField(SeriesDisplay, blank=True, related_name="in_charts")
    
    
    def __str__(self):
        return f"{self.id}. {self.title}"