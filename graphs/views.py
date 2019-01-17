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

def graphData(num_points):
    """
    """
    from .models import powerData
    if num_points > 100:
        raise Http404("Too many data points requested, please keep number below 100")
    else: 
        latest_data_list = powerData.objects.order_by('-Timestamp')[:num_points]
        print(latest_data_list)
        new_data_list = list(latest_data_list)
        print("\nNew list:")
        print(new_data_list)
        df = pd.DataFrame(data=new_data_list)
        print("\nNew dataframe:")
        print(df)
        return df
        
