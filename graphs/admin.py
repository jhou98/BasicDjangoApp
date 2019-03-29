from django.contrib import admin
from .models import WestEV, NorthEV, FraserEV, RoseEV, HealthEV, WestEVFuture
from .models import buildingData, buildingFuture
from .models import chargedCarsData, chargingCarsData, chargedCarsFuture, chargingCarsFuture

admin.site.register(WestEV)
admin.site.register(NorthEV)
admin.site.register(FraserEV)
admin.site.register(RoseEV)
admin.site.register(HealthEV)
admin.site.register(WestEVFuture)

admin.site.register(buildingData)
admin.site.register(buildingFuture)

admin.site.register(chargedCarsData)
admin.site.register(chargingCarsData)
admin.site.register(chargedCarsFuture)
admin.site.register(chargingCarsFuture)