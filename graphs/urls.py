from django.urls import path
from . import views

urlpatterns = [
    path(r'graphs', views.graphs, name='graphs'),
    path(r'api/data',views.ChartData.as_view(), name='chart' ),
    path(r'api/data2',views.ErrData.as_view(), name='err'),
    path(r'api/data3', views.BuildingData.as_view(), name='building'),
]