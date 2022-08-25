from django.urls import path
from . import views


urlpatterns = [
     path("", views.index),
     path("api/charts/<int:chart_id>", views.chart, name="chart")
]
