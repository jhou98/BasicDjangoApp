from django.contrib import admin
from .models import WestEV, NorthEV, FraserEV, RoseEV, HealthEV
from .models import WestEVFuture, NorthEVFuture, FraserEVFuture, RoseEVFuture,HealthEVFuture
from .models import building, buildingFuture
from .models import chargedCarsWest, chargingCarsWest, chargedCarsWestFuture, chargingCarsWestFuture
from .models import chargedCarsRose, chargingCarsRose, chargedCarsRoseFuture, chargingCarsRoseFuture
from .models import chargedCarsFraser, chargingCarsFraser, chargedCarsFraserFuture, chargingCarsFraserFuture
from .models import chargedCarsHealth, chargingCarsHealth, chargedCarsHealthFuture, chargingCarsHealthFuture
from .models import chargedCarsNorth, chargingCarsNorth, chargedCarsNorthFuture, chargingCarsNorthFuture

# Total: 32 databases 
# 5 EV parkades 
admin.site.register(WestEV)
admin.site.register(NorthEV)
admin.site.register(FraserEV)
admin.site.register(RoseEV)
admin.site.register(HealthEV)

# 5 predictions for parkades
admin.site.register(WestEVFuture)
admin.site.register(NorthEVFuture)
admin.site.register(FraserEVFuture)
admin.site.register(RoseEVFuture)
admin.site.register(HealthEVFuture)

# Building and Building prediction 
admin.site.register(building)
admin.site.register(buildingFuture)

# 4 for vehicles for each Parkade
admin.site.register(chargedCarsWest)
admin.site.register(chargingCarsWest)
admin.site.register(chargedCarsWestFuture)
admin.site.register(chargingCarsWestFuture)

admin.site.register(chargedCarsRose)
admin.site.register(chargingCarsRose)
admin.site.register(chargedCarsRoseFuture)
admin.site.register(chargingCarsRoseFuture)

admin.site.register(chargedCarsFraser)
admin.site.register(chargingCarsFraser)
admin.site.register(chargedCarsFraserFuture)
admin.site.register(chargingCarsFraserFuture)

admin.site.register(chargedCarsHealth)
admin.site.register(chargingCarsHealth)
admin.site.register(chargedCarsHealthFuture)
admin.site.register(chargingCarsHealthFuture)

admin.site.register(chargedCarsNorth)
admin.site.register(chargingCarsNorth)
admin.site.register(chargedCarsNorthFuture)
admin.site.register(chargingCarsNorthFuture)