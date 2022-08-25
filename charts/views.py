
from __future__ import annotations
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from .influxdb_helper import InfluxDbHelper
from .models import Chart, SeriesDisplay, LoraMeasurement

# Create your views here.
def index(request):
    context = {
        "charts" : Chart.objects.filter(active=True).order_by('display_priority', 'created_date' ) 
        }
    return render(request, "charts/index.html", context=context)



def get_measurement_data(lora : LoraMeasurement, timerange, period):
    measurement = lora.measurement
    dev_eui = lora.device_id
    
    influxdb_helper = InfluxDbHelper.get_instance()
    timestamps, values = influxdb_helper.get_measurement_data(time_range=timerange, 
                                    measurement=measurement, period=period, dev_eui=dev_eui)
    return timestamps, values


def chart(request, chart_id):
    
    try:
        chart = Chart.objects.get(pk=chart_id)
    except Chart.DoesNotExist:
        raise Http404("Chart does not exist.")

    if chart is None or chart.active == False:
        return { "status" : "fail",
                 "message" : f"Chart id {chart_id} not exist."} 
    
    try:
        
        timerange = request.GET.get('timerange', '')
        if timerange == '':
            timerange = "2h"
            
        period = request.GET.get('period', '')
        if period == '':
            period = "1m"
    
        data_array = []
        layout = {}
        annotations_array = []
        offset = 0
        for series_display in chart.series_displays.all():
            lora = series_display.measurement
            timestamps, values = get_measurement_data(lora, timerange=timerange, period=period)
            data = {"type" : series_display.chart_type,
                    "mode" : series_display.mode,
                    "name" : series_display.name,
                    "yaxis": series_display.yaxis,
                    "line": {
                                "color": series_display.color,
                                "width": 2,
                            },
                    "x": timestamps,
                    "y": values}
            
            data_array.append(data)
            

            
            annotation = {
                    "xref": 'paper',
                    "yref" : 'paper',
                    "x": 1.1,
                    "y": 1 - offset,
                    "xanchor": 'left',
                    "yanchor": 'middle',
                    "text": str(round(values[-1],1)),
                    "font": {
                        "family": 'Arial',
                        "size": 20,
                        
                        "color": series_display.color
                    },
                    "showarrow": False
                    }
            annotations_array.append(annotation)
            
            offset += 0.1
            
            
        layout = {
            "title": {
                "text": chart.title,
                "font": {
                        "family": 'Arial',
                        "size": chart.font_size,
                        "color": chart.color
                    }
            },
            "autosize": True,
            "xaxis": {
                "type": 'date'
            },
            "yaxis": {
                "autorange": True,
                "zeroline": False,
                "type": 'linear',
            },
            "yaxis2": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "right"
            },
            "yaxis3": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "left",
                "anchor" :"free",
                "tickfont" : {
                    "color": "red",
                    "position" : 2,
                }
            },
            "yaxis4": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "right",
                "tickfont" : {
                    "color": "red",
                    "position" : 2,
                }
            },
            "legend": {"orientation": 'h', 
                       "side": 'top'},
            # "paper_bgcolor":"LightSteelBlue",
            "margin" : dict(l=50, r=110, t=50, b=0),
            "annotations" : annotations_array,
        }   
        

        
        response = {
                    "status" : "success",
                    "id": chart.id, 
                    "data" : data_array,
                    "layout" : layout,
                    
                }
                
    except Exception as e:
        response = { "status" : "fail",
                     "message" : f"Unexpected error when get sensor data"} 

    
    return JsonResponse(response)