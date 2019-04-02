from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd 
from rest_framework.views import APIView
from rest_framework.response import Response

__timecol = 'timestamp'

def westgraph(request):
    """
    Sends the following data to our graphs page: 
    EV: current power, previous days peak power, previous months peak power\n
    Building: current power, previous days peak power, previous months peak power \n
    """
    from .controller import getCurrentPower, getDailyPeak, getMonthlyPeak

    #Get the values using our controller functions 
    ev_pwr = getCurrentPower('graphs_westev', __timecol, 'value')
    bd_pwr = getCurrentPower('graphs_building', __timecol, 'value')
    ev_daily = getDailyPeak('graphs_westev', __timecol)
    bd_daily = getDailyPeak('graphs_building', __timecol)
    ev_monthly = getMonthlyPeak('graphs_westev')
    bd_monthly = getMonthlyPeak('graphs_building')

    #Debugging Purposes
    print("current daily ev power is : ", ev_daily)
    print("current daily building power is : ",bd_daily)
    print("current ev power is : ",ev_pwr)
    print("current building power is : ",bd_pwr)
    print("current monthly ev peak is : ",ev_monthly)
    print("current monthly building peak is : ",bd_monthly)

    return render(request, 'westgraphs.html', {'curr_ev': ev_pwr, 'curr_bd': bd_pwr,'max_evdaily': ev_daily, 'max_evmonthly': ev_monthly, 'max_bddaily': bd_daily, 'max_bdmonthly': bd_monthly})

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

# Rest Framework - building data 
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
        
        my_df = getRecentData('graphs_building',96, 'Timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Building data future
class BuildingPredicted(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_buildingfuture',48, 'timestamp')
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
        
        my_df = getRecentData('graphs_westev',96, 'timestamp')
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
        
        my_df = getRecentData('graphs_roseev',96, 'timestamp')
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
        
        my_df = getRecentData('graphs_fraserev',96, 'timestamp')
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
        
        my_df = getRecentData('graphs_healthev',96, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - North Parkade EV data 
class NorthEVData(APIView):
    """
    This method is used to send 100 most recent ev data points from North Parkade as a JSON string\n
    Has built in support for authentication and permissions \n 
    See https://www.django-rest-framework.org/api-guide/views/ for more details 
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_northev',96, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - West Future EV Data 
class WestPredictedData(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_westevfuture',48, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Rose Future EV Data 
class RosePredictedData(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_roseevfuture',48, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Fraser Future EV Data 
class FraserPredictedData(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_fraserevfuture',48, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Health Future EV Data 
class HealthPredictedData(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_healthevfuture',48, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - North Future EV Data 
class NorthPredictedData(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_northevfuture',48, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charged Cars 
class chargedCarsWest(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarswest',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charging Cars 
class chargingCarsWest(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarswest',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charged Cars data
class ChargedCarsPredictedWest(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarswestfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charging Cars data  
class ChargingCarsPredictedWest(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarswestfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charged Cars 
class chargedCarsRose(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsrose',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charging Cars 
class chargingCarsRose(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsrose',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charged Cars data
class ChargedCarsPredictedRose(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsrosefuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charging Cars data  
class ChargingCarsPredictedRose(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsrosefuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charged Cars 
class chargedCarsFraser(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsfraser',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charging Cars 
class chargingCarsFraser(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsfraser',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charged Cars data
class ChargedCarsPredictedFraser(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsfraserfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charging Cars data  
class ChargingCarsPredictedFraser(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsfraserfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charged Cars 
class chargedCarsHealth(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarshealth',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charging Cars 
class chargingCarsHealth(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarshealth',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charged Cars data
class ChargedCarsPredictedHealth(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarshealthfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charging Cars data  
class ChargingCarsPredictedHealth(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarshealthfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charged Cars 
class chargedCarsNorth(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsnorth',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Charging Cars 
class chargingCarsNorth(APIView):
    """
    Method to send 96 most recent car data points as a JSON string \n 
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsnorth',96,'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charged Cars data
class ChargedCarsPredictedNorth(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargedcarsnorthfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)

# Rest Framework - Future Charging Cars data  
class ChargingCarsPredictedNorth(APIView):
    """
    This method used to send predicted values
    """ 
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        from .controller import getRecentData
        from .controller import pandasToJSON 
        
        my_df = getRecentData('graphs_chargingcarsnorthfuture',12, 'timestamp')
        data = pandasToJSON(my_df)
        return Response(data)