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
        
        #my_df = getRecentData('graphs_powerdata',100,'Timestamp')
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
        
        my_df = getRecentData('buildingdata',100, 'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - West Parkade EV data 
class WestEVData(APIView):
    """
    This method is used to send 100 most recent ev data points from West Parkade as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_westev',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Rose Parkade EV data 
class RoseEVData(APIView):
    """
    This method is used to send 100 most recent ev data points from Rose Parkade as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_roseev',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Fraser Parkade EV data 
class FraserEVData(APIView):
    """
    This method is used to send 100 most recent ev data points from Fraser Parkade as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_fraserev',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Health Parkade EV data 
class HealthEVData(APIView):
    """
    This method is used to send 100 most recent ev data points from Health Parkade as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_healthev',100, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

class carData(APIView):
    """
    Method to send 100 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_cardata',100,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)