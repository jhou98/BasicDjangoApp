from django.urls import path
from . import views

urlpatterns = [  
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),

    path(r'west', views.westgraph, name='westev'),
    
    path(r'api/west', views.WestEVData.as_view(), name='west'),
    path(r'api/rose', views.RoseEVData.as_view(), name='rose'),
    path(r'api/fraser', views.FraserEVData.as_view(), name='fraser'),
    path(r'api/health', views.HealthEVData.as_view(), name='health'),
    path(r'api/north', views.NorthEVData.as_view(), name='north'),

    path(r'api/building', views.BuildingData.as_view(), name='building'),
    path(r'api/prediction/building', views.BuildingPredicted.as_view(), name='building_future'),

    path(r'api/prediction/west', views.WestPredictedData.as_view(), name='west_future'),
    path(r'api/prediction/rose', views.RosePredictedData.as_view(), name='rose_future'),
    path(r'api/prediction/fraser', views.FraserPredictedData.as_view(), name='fraser_future'),
    path(r'api/prediction/health', views.HealthPredictedData.as_view(), name='health_future'),
    path(r'api/prediction/north', views.NorthPredictedData.as_view(), name='north_future'),

    path(r'api/chargedcars/west',views.chargedCarsWest.as_view(), name='carschargedwest'),
    path(r'api/chargingcars/west',views.chargingCarsWest.as_view(), name='carschargingwest'),
    path(r'api/prediction/chargedcars/west',views.ChargedCarsPredictedWest.as_view(), name='carschargedwest_future'),
    path(r'api/prediction/chargingcars/west',views.ChargingCarsPredictedWest.as_view(), name='carschargingwest_future'),

    path(r'api/chargedcars/rose',views.chargedCarsRose.as_view(), name='carschargedrose'),
    path(r'api/chargingcars/rose',views.chargingCarsRose.as_view(), name='carschargingrose'),
    path(r'api/prediction/chargedcars/rose',views.ChargedCarsPredictedRose.as_view(), name='carschargedrose_future'),
    path(r'api/prediction/chargingcars/rose',views.ChargingCarsPredictedRose.as_view(), name='carschargingrose_future'),

    path(r'api/chargedcars/fraser',views.chargedCarsFraser.as_view(), name='carschargedfraser'),
    path(r'api/chargingcars/fraser',views.chargingCarsFraser.as_view(), name='carschargingfraser'),
    path(r'api/prediction/chargedcars/fraser',views.ChargedCarsPredictedFraser.as_view(), name='carschargedfraser_future'),
    path(r'api/prediction/chargingcars/fraser',views.ChargingCarsPredictedFraser.as_view(), name='carschargingfraser_future'),

    path(r'api/chargedcars/health',views.chargedCarsHealth.as_view(), name='carschargedhealth'),
    path(r'api/chargingcars/health',views.chargingCarsHealth.as_view(), name='carscharginghealth'),
    path(r'api/prediction/chargedcars/health',views.ChargedCarsPredictedHealth.as_view(), name='carschargedhealth_future'),
    path(r'api/prediction/chargingcars/health',views.ChargingCarsPredictedHealth.as_view(), name='carscharginghealth_future'),

    path(r'api/chargedcars/north',views.chargedCarsNorth.as_view(), name='carschargednorth'),
    path(r'api/chargingcars/north',views.chargingCarsNorth.as_view(), name='carschargingnorth'),
    path(r'api/prediction/chargedcars/north',views.ChargedCarsPredictedNorth.as_view(), name='carschargednorth_future'),
    path(r'api/prediction/chargingcars/north',views.ChargingCarsPredictedNorth.as_view(), name='carschargingnorth_future'),
  
]

