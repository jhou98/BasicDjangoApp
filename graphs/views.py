from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pandas as pd 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes


class graph():

    def getevgraph(x):
        return { 
            'west': 'graphs_westev',
            'rose': 'graphs_roseev',
            'fraser': 'graphs_fraserev',
            'health': 'graphs_healthev',
            'north': 'graphs_northev',
        } [x]

    def getgraph(request, parkade, template ):
        """
        Sends the following data to our graphs page: 
        EV: current power, previous days peak power, previous months peak power\n
        Building: current power, previous days peak power, previous months peak power \n
        """
        from .controller import getCurrentPower, getDailyPeak, getMonthlyPeak
        __timecol = 'timestamp'
        graphval = graph.getevgraph(parkade)
        #Get the values using our controller functions 
        ev_pwr = getCurrentPower(graphval, __timecol, 'value')
        bd_pwr = getCurrentPower('graphs_buildingwest', __timecol, 'value')
        ev_daily = getDailyPeak(graphval, __timecol)
        bd_daily = getDailyPeak('graphs_buildingwest', __timecol)
        ev_monthly = getMonthlyPeak(graphval)
        bd_monthly = getMonthlyPeak('graphs_buildingwest')

        return render(request, template, {'curr_ev': ev_pwr, 'curr_bd': bd_pwr,'max_evdaily': ev_daily, 'max_evmonthly': ev_monthly, 'max_bddaily': bd_daily, 'max_bdmonthly': bd_monthly})

    def westgraph(request):
        return graph.getgraph(request, 'west', 'westgraphs.html')

    def rosegraph(request):
        return graph.getgraph(request, 'rose', 'rosegraphs.html')
    
    def frasergraph(request):
        return graph.getgraph(request, 'fraser', 'frasergraphs.html')

    def healthgraph(request):
        return graph.getgraph(request, 'health', 'healthgraphs.html')

    def northgraph(request):
        return graph.getgraph(request, 'north', 'northgraphs.html')

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

@api_view(['GET'])    
@renderer_classes((JSONRenderer,))
def getJSONData(request, location, format=None):
    """
    A view that returns the count of active users in JSON.
    """
    from .controller import getRecentData
    from .controller import pandasToJSON 
    my_df = getRecentData(location, 96, 'timestamp')
    return Response(my_df)

@api_view(['GET'])    
@renderer_classes((JSONRenderer,))
def getJSONPredictedData(request, location, format=None):
    """
    A view that returns the count of active users in JSON.
    """
    from .controller import getRecentData
    from .controller import pandasToJSON 
    my_df = getRecentData(location, 48, 'timestamp')
    return Response(my_df)

class BuildingData():
    
    def getbdgraph(x):
        return { 
            'west': 'graphs_buildingwest',
            'rose': 'graphs_buildingrose',
            'fraser': 'graphs_buildingfraser',
            'health': 'graphs_buildinghealth',
            'north': 'graphs_buildingnorth',
        } [x]

    def west(request):
        mygraph = BuildingData.getgraph('west')
        return getJSONData(request, mygraph)

    def rose(request):
        mygraph = BuildingData.getgraph('rose')
        return getJSONData(request, mygraph)

    def fraser(request):
        mygraph = BuildingData.getgraph('fraser')
        return getJSONData(request, mygraph)

    def health(request):
        mygraph = BuildingData.getgraph('health')
        return getJSONData(request, mygraph)

    def north(request):
        mygraph = BuildingData.getgraph('north')
        return getJSONData(request, mygraph)

# Rest Framework - Building data future
class BuildingPredictedData:

    def getgraph(x):
        return { 
            'west': 'graphs_buildingwestfuture',
            'rose': 'graphs_buildingrosefuture',
            'fraser': 'graphs_buildingfraserfuture',
            'health': 'graphs_buildinghealthfuture',
            'north': 'graphs_buildingnorthfuture',
        } [x]

    def west(request):
        mygraph = BuildingPredictedData.getgraph('west')
        return getJSONPredictedData(request, mygraph)

    def rose(request):
        mygraph = BuildingPredictedData.getgraph('rose')
        return getJSONPredictedData(request, mygraph)

    def fraser(request):
        mygraph = BuildingPredictedData.getgraph('fraser')
        return getJSONPredictedData(request, mygraph)

    def health(request):
        mygraph = BuildingPredictedData.getgraph('health')
        return getJSONPredictedData(request, mygraph)

    def north(request):
        mygraph = BuildingPredictedData.getgraph('north')
        return getJSONPredictedData(request, mygraph)

# Rest Framework - Ev data
class EVData():
    """
        Class for EV data 
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_westev',
            'rose': 'graphs_roseev',
            'fraser': 'graphs_fraserev',
            'health': 'graphs_healthev',
            'north': 'graphs_northev',
        } [x]

    def west(request):
        mygraph = EVData.getgraph('west')
        return getJSONData(request, mygraph)

    def rose(request):
        mygraph = EVData.getgraph('rose')
        return getJSONData(request, mygraph)

    def fraser(request):
        mygraph = EVData.getgraph('fraser')
        return getJSONData(request, mygraph)

    def health(request):
        mygraph = EVData.getgraph('health')
        return getJSONData(request, mygraph)

    def north(request):
        mygraph = EVData.getgraph('north')
        return getJSONData(request, mygraph)

# Rest Framework - Ev data
class EVPredictedData():
    """
        Class for EV data predicted
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_westevfuture',
            'rose': 'graphs_roseevfuture',
            'fraser': 'graphs_fraserevfuture',
            'health': 'graphs_healthevfuture',
            'north': 'graphs_northevfuture',
        } [x]

    def west(request):
        mygraph = EVPredictedData.getgraph('west')
        return getJSONPredictedData(request, mygraph)

    def rose(request):
        mygraph = EVPredictedData.getgraph('rose')
        return getJSONPredictedData(request, mygraph)

    def fraser(request):
        mygraph = EVPredictedData.getgraph('fraser')
        return getJSONPredictedData(request, mygraph)

    def health(request):
        mygraph = EVPredictedData.getgraph('health')
        return getJSONPredictedData(request, mygraph)

    def north(request):
        mygraph = EVPredictedData.getgraph('north')
        return getJSONPredictedData(request, mygraph)

# Rest Framework - Charged Cars 
class chargedCarsData():
    """
        Class for charged cars
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_chargedcarswest',
            'rose': 'graphs_chargedcarsrose',
            'fraser': 'graphs_chargedcarsfraser',
            'health': 'graphs_chargedcarshealth',
            'north': 'graphs_chargedcarsnorth',
        } [x]

    def west(request):
        mygraph = chargedCarsData.getgraph('west')
        return getJSONData(request, mygraph)

    def rose(request):
        mygraph = chargedCarsData.getgraph('rose')
        return getJSONData(request, mygraph)

    def fraser(request):
        mygraph = chargedCarsData.getgraph('fraser')
        return getJSONData(request, mygraph)

    def health(request):
        mygraph = chargedCarsData.getgraph('health')
        return getJSONData(request, mygraph)

    def north(request):
        mygraph = chargedCarsData.getgraph('north')
        return getJSONData(request, mygraph)

# Rest Framework - Charged cars predicted 
class chargedCarsPredictedData():
    """
        Class for charged cars predicted
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_chargedcarswestfuture',
            'rose': 'graphs_chargedcarsrosefuture',
            'fraser': 'graphs_chargedcarsfraserfuture',
            'health': 'graphs_chargedcarshealthfuture',
            'north': 'graphs_chargedcarsnorthfuture',
        } [x]

    def west(request):
        mygraph = chargedCarsPredictedData.getgraph('west')
        return getJSONPredictedData(request, mygraph)

    def rose(request):
        mygraph = chargedCarsPredictedData.getgraph('rose')
        return getJSONPredictedData(request, mygraph)

    def fraser(request):
        mygraph = chargedCarsPredictedData.getgraph('fraser')
        return getJSONPredictedData(request, mygraph)

    def health(request):
        mygraph = chargedCarsPredictedData.getgraph('health')
        return getJSONPredictedData(request, mygraph)

    def north(request):
        mygraph = chargedCarsPredictedData.getgraph('north')
        return getJSONPredictedData(request, mygraph)

# Rest Framework - Charging Cars
class chargingCarsData():
    """
        Class for charging cars
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_chargingcarswest',
            'rose': 'graphs_chargingcarsrose',
            'fraser': 'graphs_chargingcarsfraser',
            'health': 'graphs_chargingcarshealth',
            'north': 'graphs_chargingcarsnorth',
        } [x]

    def west(request):
        mygraph = chargingCarsData.getgraph('west')
        return getJSONData(request, mygraph)

    def rose(request):
        mygraph = chargingCarsData.getgraph('rose')
        return getJSONData(request, mygraph)

    def fraser(request):
        mygraph = chargingCarsData.getgraph('fraser')
        return getJSONData(request, mygraph)

    def health(request):
        mygraph = chargingCarsData.getgraph('health')
        return getJSONData(request, mygraph)

    def north(request):
        mygraph = chargingCarsData.getgraph('north')
        return getJSONData(request, mygraph)

# Rest Framework - Charging Cars predicted 
class chargingCarsPredictedData():
    """
        Class for charging cars predicted
    """
    
    def getgraph(x):
        """
            Gets the graph 
        """
        return { 
            'west': 'graphs_chargingcarswestfuture',
            'rose': 'graphs_chargingcarsrosefuture',
            'fraser': 'graphs_chargingcarsfraserfuture',
            'health': 'graphs_chargingcarshealthfuture',
            'north': 'graphs_chargingcarsnorthfuture',
        } [x]

    def west(request):
        mygraph = chargingCarsPredictedData.getgraph('west')
        return getJSONPredictedData(request, mygraph)

    def rose(request):
        mygraph = chargingCarsPredictedData.getgraph('rose')
        return getJSONPredictedData(request, mygraph)

    def fraser(request):
        mygraph = chargingCarsPredictedData.getgraph('fraser')
        return getJSONPredictedData(request, mygraph)

    def health(request):
        mygraph = chargingCarsPredictedData.getgraph('health')
        return getJSONPredictedData(request, mygraph)

    def north(request):
        mygraph = chargingCarsPredictedData.getgraph('north')
        return getJSONPredictedData(request, mygraph)