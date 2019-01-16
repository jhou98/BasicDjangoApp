from django.shortcuts import render
from django.http import HttpResponse

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
    #output = ', '.join([d.Power for d in latest_data_list])
    return render(request, 'data.html', {'recent_data':latest_data_list})

def peakData(request, num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted
    """
    from .models import powerData 
    latest_data_list = powerData.objects.order_by('-Power')[:num_req]
    return render(request, 'max_val.html', {'max_power':latest_data_list})
