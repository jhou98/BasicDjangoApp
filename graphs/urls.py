from django.urls import path
from . import views

urlpatterns = [
    path(r'graphs', views.graphs, name='graphs'),
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),
    path(r'date/<str:date_val>/',views.dateData, name='date'),
    path(r'api/building', views.BuildingData.as_view(), name='building'),
    path(r'api/west', views.WestEVData.as_view(), name='west'),
    path(r'api/rose', views.RoseEVData.as_view(), name='rose'),
    path(r'api/fraser', views.FraserEVData.as_view(), name='fraser'),
    path(r'api/health', views.HealthEVData.as_view(), name='health'),
    path(r'api/chargedcars',views.chargedCars.as_view(), name='carscharged'),
    path(r'api/chargingcars',views.chargingCars.as_view(), name='carscharging'),
    path(r'api/prediction/chargedcars',views.ChargedCarsPredicted.as_view(), name='carscharged_future'),
    path(r'api/prediction/chargingcars',views.ChargingCarsPredicted.as_view(), name='carscharging_future'),
    path(r'api/prediction/building', views.BuildingPredicted.as_view(), name='building_future'),
    path(r'api/prediction/west', views.WestPredictedData.as_view(), name='west_future'),
]