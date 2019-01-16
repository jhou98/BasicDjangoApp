from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recent/<int:num_req>/',views.recentData, name='recent'),
    path('max/<int:num_req>/',views.peakData, name='max')
]