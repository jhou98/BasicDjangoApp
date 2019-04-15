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
        """
        Dictionary of Key-Value pairs for parkades. 

        @returns string for our table name in the database 
        """
        return { 
            'west': 'graphs_westev',
            'rose': 'graphs_roseev',
            'fraser': 'graphs_fraserev',
            'health': 'graphs_healthev',
            'north': 'graphs_northev',
        } [x]

    def getbdgraph(x):
        """
        Dictionary of Key-Value pairs for buildings. 

        @returns string for our table name in the database 
        """
        return {
            'west': 'graphs_buildingwest',
            'rose': 'graphs_buildingrose',
            'fraser': 'graphs_buildingfraser',
            'health': 'graphs_buildinghealth',
            'north': 'graphs_buildingnorth',
        } [x]

    def getgraph(request, parkade, template):
        """
        Sends the following data to our graphs page: 

        EV: current power, previous days peak power, previous months peak power

        Building: current power, previous days peak power, previous months peak power 
        """
        from .controller import getCurrentPower, getDailyPeak, getMonthlyPeak
        __timecol = 'timestamp'
        __val = 'value'
        evgraphs = graph.getevgraph(parkade)
        bdgraphs = graph.getbdgraph(parkade)
        #Get the values using our controller functions 
        ev_pwr = getCurrentPower(evgraphs, __timecol, __val)
        bd_pwr = getCurrentPower(bdgraphs, __timecol, __val)
        ev_daily = getDailyPeak(evgraphs, __timecol)
        bd_daily = getDailyPeak(bdgraphs, __timecol)
        ev_monthly = getMonthlyPeak(evgraphs)
        bd_monthly = getMonthlyPeak(bdgraphs)

        return render(request, template, {'curr_ev': ev_pwr, 'curr_bd': bd_pwr,'max_evdaily': ev_daily, 'max_evmonthly': ev_monthly, 'max_bddaily': bd_daily, 'max_bdmonthly': bd_monthly})

    """
    The following functions are specific to each parkade, and uses the other functions in the graph class to get the values that we need for our main chart pages. 

    @returns a render which graphs our request to a URL and HTML template.
    """
    def west(request):
        return graph.getgraph(request, 'west', 'westgraphs.html')

    def rose(request):
        return graph.getgraph(request, 'rose', 'rosegraphs.html')
    
    def fraser(request):
        return graph.getgraph(request, 'fraser', 'frasergraphs.html')

    def health(request):
        return graph.getgraph(request, 'health', 'healthgraphs.html')

    def north(request):
        return graph.getgraph(request, 'north', 'northgraphs.html')

@api_view(['GET'])    
@renderer_classes((JSONRenderer,))
def getJSONData(request, location, format=None):
    """
    Returns a response in JSON. 
    
    To control the amount of datapoints (rows), modify the function getRecentData(*graphname, *num of points, *name of column to order by)
    """
    from .controller import getRecentData
    my_df = getRecentData(location, 96, 'timestamp')
    return Response(my_df)

@api_view(['GET'])    
@renderer_classes((JSONRenderer,))
def getJSONPredictedData(request, location, format=None):
    """
    Returns a response in JSON, this is a seperate function as predicted is 12 hours instead of 24. 
    
    To control the amount of datapoints (rows), modify the function getRecentData(*graphname, *num of points, *name of column to order by)
    """
    from .controller import getRecentData
    my_df = getRecentData(location, 48, 'timestamp')
    return Response(my_df)


"""
The classes below are all similar, with the following functions. 
getgraph(x): Dictionary that maps parkade to the name of the table in my sql. 
west(request)
rose(request)
fraser(request)
health(request)
north(request): returns a JSON response of data to the url request. 

self / parent classes are not used because of how these functions are called in urls.py
if self is used, an error occurs in urls.py as it then needs a request argument explicitly stated 
"""
class BuildingData():
     
    def getgraph(x):
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

    def getgraph(x):

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

# Rest Framework - Ev data future
class EVPredictedData():
    
    def getgraph(x):

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
    
    def getgraph(x):
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
    
    def getgraph(x):
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
    
    def getgraph(x):
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
    
    def getgraph(x):
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