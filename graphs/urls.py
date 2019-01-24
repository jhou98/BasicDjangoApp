from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'recent/<int:num_req>/',views.recentData, name='recent'),
    path(r'max/<int:num_req>/',views.peakData, name='max'),
    path(r'date/<str:date_val>/',views.dateData, name='date'),
    path(r'api/data',views.ChartData.as_view(), name='chart' ),
]