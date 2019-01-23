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
    from graphs.controller import getBaseData
    return render(request, 'graphs.html', {'test_fn': getBaseData('graphs_powerdata')})

def recentData(request, num_req):
    """
    Gets a list of the most recent data points in our powerData table model \n
    :param int num_req: Number of data points to extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .models import powerData 
    if num_req > 1000:
        raise Http404("Error, too many datapoints requested. MAX = 1000")
    latest_data_list = powerData.objects.order_by('-Timestamp')[:num_req]
    return render(request, 'data.html', {'recent_data':latest_data_list})

def peakData(request, num_req):
    """
    Gets a list of data points ordered by power consumption \n
    :param int num_req: Number of data points to be extracted \n
    Returns an unordered list of datapoints (max of 1000)
    """
    from .models import powerData 
    if num_req > 1000:
        raise Http404("Error, too many datapoints requested. MAX = 1000")
    latest_data_list = powerData.objects.order_by('-Power')[:num_req]
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

# matplotlib graph
def GraphData(request):
    from .models import powerData
    from chartit import DataPool, Chart

    #Create the datapool with data we wish to retrieve 
    powerdata = DataPool(
                    series= [{ 'options': {
                            'source': powerData.objects.order_by('-Timestamp')[:100]},
                            'terms':[
                                'Timestamp',
                                'Power'
                            ]}
                        ])

    #Create the chart object 
    powerchart = Chart(
                    datasource = powerdata,
                    series_options = 
                        [{'options':{
                            'type':'line',
                            'stacking': False},
                        'terms':{
                            'Timestamp':[
                            'Power']
                        }}],
                    chart_options = 
                        {'title': {
                            'text': 'EV Power Data' },
                        'xAxis': {'title': {
                            'text': 'Date' }},
                        'yAxis': {'title': {
                            'text': 'Power Generated' }}})

    return render(request, 'graphs.html',{'powerchart':powerchart})

# Rest Framework 
class ChartData(APIView):
    """
    This method is similar to our getData method \n
    However it has built in support for authentication and permissions \n 
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