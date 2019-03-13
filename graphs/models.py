from django.db import models

class EVData(models.Model):
    """
    Class that represents EV data and has the following: 
        1. timestamp: Datetime field and primary key
        2. value: Energy value in kwh
    See https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateField for more details on the models
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.DecimalField(max_digits = 15, decimal_places = 5)

    """
        Returns a string of the following format
        Date: MM/DD/YYYY Time: HH:MM:SS kW: #
    """
    def __str__(self):
        return "Date: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "  Power: " + str(self.value)

class BDData(models.Model):
    """
    Class that represents building data and has the following: 
        1. timestamp: Datetime field and primary key
        2. value: Energy value in kw
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.DecimalField(max_digits = 15, decimal_places = 5)

    def __str__(self):
        return "Date: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "  Power: " + str(self.value)

##Create two seperate classes: EV and Building so we have two separate databases to hold our data 
