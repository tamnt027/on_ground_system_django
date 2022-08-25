
from django.db import models

class ChartMode(models.TextChoices):
    Lines = 'lines'
    # Markers = 'markers'
    LinesMarkers = 'lines+markers'


class ChartType(models.TextChoices):
    Scatter = 'scatter'

    
class YAxisType(models.TextChoices):
    YAxisLeft = 'y1'
    YAxisRight = 'y2'
    
    