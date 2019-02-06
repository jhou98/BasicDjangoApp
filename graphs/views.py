from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd 
from rest_framework.views import APIView
from rest_framework.response import Response

def graphs(request):
    """
    Home Page \n 
    This will be modified to send the following data: \n
    Current Power \n 
    peakDaily power \n
    peakMonthly power \n 
    """
    from .controller import getCurrentPower, getDailyPeak, getMonthlyPeak

    #Get the values using our controller functions 
    ev_pwr = getCurrentPower('graphs_powerdata')
    bd_pwr = getCurrentPower('graphs_powerdata')
    ev_daily = getDailyPeak('graphs_powerdata')
    bd_daily = getDailyPeak('graphs_powerdata')
    ev_monthly = getMonthlyPeak('graphs_powerdata')
    bd_monthly = getMonthlyPeak('graphs_powerdata')

    #Compare to set our max for our gauges
    if ev_pwr > ev_daily: 
        daily_evpwr = ev_pwr
    else: 
        daily_evpwr = ev_daily
    
    if bd_pwr > bd_daily: 
        daily_bdpwr = bd_pwr
    else:
        daily_bdpwr = bd_daily

    if ev_pwr > ev_monthly: 
        monthly_evpwr = ev_pwr
    else: 
        monthly_evpwr = ev_monthly
    
    if bd_pwr > bd_monthly: 
        monthly_bdpwr = bd_pwr
    else:
        monthly_bdpwr = bd_monthly

    #Debugging Purposes
    print("current daily ev power is : ", daily_evpwr)
    print("current daily building power is : ",daily_bdpwr)
    print("current ev power is : ",ev_pwr)
    print("current building power is : ",bd_pwr)
    print("current monthly peak is : ",monthly_evpwr)
    print("current monthly peak is : ",monthly_bdpwr)

    return render(request, 'graphs.html', {'curr_ev': ev_pwr, 'curr_bd': bd_pwr,'max_evdaily': daily_evpwr, 'max_evmonthly': monthly_evpwr, 'max_bddaily': daily_bdpwr, 'max_bdmonthly': monthly_bdpwr})

def recentData(request, num_req):
    """
    Gets a list of the most recent data points in our powerData table model \n
    :param int num_req: Number of data points to extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .controller import getRecentDataList as getRecent
    if num_req > 1000:
        raise Http404("Too many points requested. MAX=1000")
    latest_data_list = getRecent(num_req)
    return render(request, 'data.html', {'recent_data':latest_data_list})

def peakData(request, num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .controller import getMaxData 
    if num_req > 1000:
        raise Http404("Too many points requested. MAX=1000")
    latest_data_list = getMaxData(num_req)
    return render(request, 'max_val.html', {'max_power':latest_data_list})

def dateData(request, date_val):
    """
    Gets a list of data points corresponding to the specific date \n
    :param Datetime date_val: Date in YYYY-MM-DD format
    Returns an unorder list of datapoints, error if date does not exist
    """
    from .controller import getSingleDateData as getDateData
    my_df = getDateData('graphs_powerdata','Timestamp',date_val)
    if my_df.empty: 
        raise Http404("Timestamp does not exist!")
    return render(request, 'date.html', {'date': date_val, 'date_data':my_df})

# Rest Framework v1
class ChartData(APIView):
    """
    This method is used to send 100 most recent data points as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_powerdata',100,'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest framework v2
class ErrData(APIView):
    """
    This method takes our trial data points with error as a JSON string \n
    Similar to ChartData class 
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('powererr',96,'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)