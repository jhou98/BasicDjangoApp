from django.contrib import admin
from .models import EVData
from .models import powerData

admin.site.register(EVData)
admin.site.register(powerData)
