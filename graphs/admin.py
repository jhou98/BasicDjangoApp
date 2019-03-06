from django.contrib import admin
from .models import powerData, EVEnergy, BuildingEnergy, WestEV, NorthEV, FraserEV, RoseEV, HealthEV

admin.site.register(powerData)
admin.site.register(EVEnergy)
admin.site.register(BuildingEnergy)
admin.site.register(WestEV)
admin.site.register(NorthEV)
admin.site.register(FraserEV)
admin.site.register(RoseEV)
admin.site.register(HealthEV)