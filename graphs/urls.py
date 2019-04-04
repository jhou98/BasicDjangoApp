from django.urls import path
from . import views

urlpatterns = [  
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),

    path(r'west', views.graph.westgraph, name='westev'),
    path(r'rose', views.graph.rosegraph, name='roseev'),
    path(r'fraser', views.graph.frasergraph, name='fraserev'),
    path(r'health', views.graph.healthgraph, name='healthev'),
    path(r'north', views.graph.northgraph, name='northev'), #No data currently 

    path(r'api/west', views.EVData.west, name='west'),
    path(r'api/rose', views.EVData.rose, name='rose'),
    path(r'api/fraser', views.EVData.fraser, name='fraser'),
    path(r'api/health', views.EVData.health, name='health'),
    path(r'api/north', views.EVData.north, name='north'),

    path(r'api/prediction/west', views.EVPredictedData.west, name='west_future'),
    path(r'api/prediction/rose', views.EVPredictedData.rose, name='rose_future'),
    path(r'api/prediction/fraser', views.EVPredictedData.fraser, name='fraser_future'),
    path(r'api/prediction/health', views.EVPredictedData.health, name='health_future'),
    path(r'api/prediction/north', views.EVPredictedData.north, name='north_future'),

    path(r'api/buildingwest', views.BuildingData.west, name='buildingwest'),
    path(r'api/buildingrose', views.BuildingData.rose, name='buildingrose'),
    path(r'api/buildingfraser', views.BuildingData.fraser, name='buildingfraser'),
    path(r'api/buildinghealth', views.BuildingData.health, name='buildinghealth'),
    path(r'api/buildingnorth', views.BuildingData.north, name='buildingnorth'),

    path(r'api/prediction/buildingwest', views.BuildingPredictedData.west, name='buildingwest_future'),
    path(r'api/prediction/buildingrose', views.BuildingPredictedData.rose, name='buildingrose_future'),
    path(r'api/prediction/buildingfraser', views.BuildingPredictedData.fraser, name='buildingfraser_future'),
    path(r'api/prediction/buildinghealth', views.BuildingPredictedData.health, name='buildinghealth_future'),
    path(r'api/prediction/buildingnorth', views.BuildingPredictedData.north, name='buildingnorth_future'),

    path(r'api/chargedcars/west',views.chargedCarsData.west, name='carschargedwest'),
    path(r'api/chargedcars/rose',views.chargedCarsData.rose, name='carschargedrose'),
    path(r'api/chargedcars/fraser',views.chargedCarsData.fraser, name='carschargedfraser'),
    path(r'api/chargedcars/health', views.chargedCarsData.health, name='carschargedhealth'),
    path(r'api/chargedcars/north', views.chargedCarsData.north, name='carschargednorth'),

    path(r'api/prediction/chargedcars/west', views.chargedCarsPredictedData.west, name='carschargedwest_future'),
    path(r'api/prediction/chargedcars/rose', views.chargedCarsPredictedData.rose, name='carschargedrose_future'),
    path(r'api/prediction/chargedcars/fraser', views.chargedCarsPredictedData.fraser, name='carschargedfraser_future'),
    path(r'api/prediction/chargedcars/health', views.chargedCarsPredictedData.health, name='carschargedhealth_future'),
    path(r'api/prediction/chargedcars/north', views.chargedCarsPredictedData.north, name='carschargednorth_future'),

    path(r'api/chargingcars/west',views.chargingCarsData.west, name='carschargingwest'),
    path(r'api/chargingcars/rose',views.chargingCarsData.rose, name='carschargingrose'),
    path(r'api/chargingcars/fraser',views.chargingCarsData.fraser, name='carschargingfraser'),
    path(r'api/chargingcars/health', views.chargingCarsData.health, name='carscharginghealth'),
    path(r'api/chargingcars/north', views.chargingCarsData.north, name='carschargingnorth'),

    path(r'api/prediction/chargingcars/west', views.chargingCarsPredictedData.west, name='carschargingwest_future'),
    path(r'api/prediction/chargingcars/rose', views.chargingCarsPredictedData.rose, name='carschargingrose_future'),
    path(r'api/prediction/chargingcars/fraser', views.chargingCarsPredictedData.fraser, name='carschargingfraser_future'),
    path(r'api/prediction/chargingcars/health', views.chargingCarsPredictedData.health, name='carscharginghealth_future'),
    path(r'api/prediction/chargingcars/north', views.chargingCarsPredictedData.north, name='carschargingnorth_future')
]

