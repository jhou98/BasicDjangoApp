from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd 
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    """
    Home Page \n 
    This will be modified accordingly in the future
    """
    from .controller import getBaseData
    return render(request, 'graphs.html', {'test_fn': getBaseData('graphs_powerdata')})

def recentData(request, num_req):
    """
    Gets a list of the most recent data points in our powerData table model \n
    :param int num_req: Number of data points to extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .controller import getRecentDataList as getRecent
    latest_data_list = getRecent(num_req)
    return render(request, 'data.html', {'recent_data':latest_data_list})

def peakData(request, num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .controller import getMaxData 
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
        
        my_df = getRecentData('powererr',98,'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)