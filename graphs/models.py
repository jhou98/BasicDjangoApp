from django.db import models

"""
    Class that represents EV data and has the following: 
        1. Date - in Date format 
        2. Time - in Time format 
        3. kW - up to 999 with 3 decimal places
    See https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateField for more details on the models
"""
class EVData(models.Model):
    data_date = models.DateField()
    data_time = models.TimeField() 
    data_kW = models.DecimalField(max_digits = 6, decimal_places = 3)

    """
        Returns a string of the following format
        Date: MM/DD/YYYY Time: HH:MM:SS kW: #
    """
    def __str__(self):
        return "Date: " + self.data_date.strftime('%m/%d/%Y') + " Time: " + self.data_time.strftime('%H:%M:%S')  + " kW: " + str(self.data_kW)