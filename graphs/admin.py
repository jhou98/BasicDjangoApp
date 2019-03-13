from django.contrib import admin
from .models import EVData
from .models import BDData

admin.site.register(EVData)
admin.site.register(BDData)
