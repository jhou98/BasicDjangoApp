from django.urls import path
from . import views

urlpatterns = [
    path('', views.graphs, name='graphs'),
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),
    path(r'date/<str:date_val>/',views.dateData, name='date'),
    path(r'api/data',views.ChartData.as_view(), name='chart' ),
    path(r'api/data2',views.ErrData.as_view(), name='err'),
    path(r'api/data3', views.BuildingData.as_view(), name='building'),
]