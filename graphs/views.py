from django.shortcuts import render
from django.http import HttpResponse, Http404
import pandas as pd 

def index(request):
    """
    Home Page \n 
    This will be modified accordingly in the future
    """
    from graphs.query import baseData
    return render(request, 'graphs.html', {'test_fn': baseData('graphs_powerdata')})

def recentData(request, num_req):
    """
    Gets a list of the most recent data points in our powerData table model \n
    :param int num_req: Number of data points to extracted
    """
    from .models import powerData 
    latest_data_list = powerData.objects.order_by('-Timestamp')[:num_req]
    return render(request, 'data.html', {'recent_data':latest_data_list})

def peakData(request, num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted
    """
    from .models import powerData 
    latest_data_list = powerData.objects.order_by('-Power')[:num_req]
    return render(request, 'max_val.html', {'max_power':latest_data_list})

def dateData(request, date_val):
    """
    Gets a list of data points corresponding to the specific date \n
    :param Datetime date_val: Date in YYYY-MM-DD format
    """
    from .query import singleDateData as getData
    my_df = getData('graphs_powerdata','Timestamp',date_val)
    if my_df.empty: 
        raise Http404("Timestamp does not exist!")
    return render(request, 'date.html', {'date': date_val, 'date_data':my_df})
        
