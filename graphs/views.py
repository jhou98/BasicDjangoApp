from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd 
from rest_framework.views import APIView
from rest_framework.response import Response

__timecol = 'timestamp'

def graphs(request):
    """
    Sends the following data to our graphs page: 
    EV: current power, previous days peak power, previous months peak power\n
    Building: current power, previous days peak power, previous months peak power \n
    """
    from .controller import getCurrentPower, getDailyPeak, getMonthlyPeak

    #Get the values using our controller functions 
    ev_pwr = getCurrentPower('testtable', __timecol, 'value')
    bd_pwr = getCurrentPower('buildingdata', __timecol, 'value')
    ev_daily = getDailyPeak('testtable', __timecol)
    bd_daily = getDailyPeak('buildingdata', __timecol)
    ev_monthly = getMonthlyPeak('testtable')
    bd_monthly = getMonthlyPeak('buildingdata')

    #Debugging Purposes
    print("current daily ev power is : ", ev_daily)
    print("current daily building power is : ",bd_daily)
    print("current ev power is : ",ev_pwr)
    print("current building power is : ",bd_pwr)
    print("current monthly ev peak is : ",ev_monthly)
    print("current monthly building peak is : ",bd_monthly)

    return render(request, 'graphs.html', {'curr_ev': ev_pwr, 'curr_bd': bd_pwr,'max_evdaily': ev_daily, 'max_evmonthly': ev_monthly, 'max_bddaily': bd_daily, 'max_bdmonthly': bd_monthly})


# Rest Framework v1 - ev data 
class ChartData(APIView):
    """
    This method is used to send 100 most recent ev data points as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('testtable',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest framework v2 - error bars 
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

# Rest Framework v3 - building data 
class BuildingData(APIView):
    """
    This method is used to send 100 most recent building data points as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('buildingdata',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)