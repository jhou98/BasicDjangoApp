from django.urls import path
from . import views

urlpatterns = [
    path(r'graphs', views.graphs, name='graphs'),
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),
    path(r'date/<str:date_val>/',views.dateData, name='date'),
    path(r'api/data',views.ChartData.as_view(), name='chart' ),
    path(r'api/data2',views.ErrData.as_view(), name='err'),
    path(r'api/data3', views.BuildingData.as_view(), name='building'),
    path(r'api/west', views.WestEVData.as_view(), name='west'),
    path(r'api/rose', views.RoseEVData.as_view(), name='rose'),
    path(r'api/fraser', views.FraserEVData.as_view(), name='fraser'),
    path(r'api/health', views.HealthEVData.as_view(), name='health'),
    path(r'api/cars',views.carData.as_view(), name='cars'),
    path(r'api/prediction/west', views.WestPredictedData.as_view(), name='west_future'),
]