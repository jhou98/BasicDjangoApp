from django.db import models

class EVData(models.Model):
    """
    Class that represents EV data and has the following: 
        1. data_date - in Date format 
        2. data_time - in Time format 
        3. data_kW - up to 999 with 3 decimal places
    See https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateField for more details on the models
    """
    data_date = models.DateField()
    data_time = models.TimeField() 
    data_kW = models.DecimalField(max_digits = 8, decimal_places = 3)

    """
        Returns a string of the following format
        Date: MM/DD/YYYY Time: HH:MM:SS kW: #
    """
    def __str__(self):
        return "Date: " + self.data_date.strftime('%m/%d/%Y') + " Time: " + self.data_time.strftime('%H:%M:%S')  + " kW: " + str(self.data_kW)

class powerData(models.Model):
    """
    Class that holds 3 variables
        1. index 
        2. Timestamp: DateTime
        3. Power: Decimal(max digits = 8, decimal places = 3)
    """
    index = models.AutoField(primary_key=True)
    Timestamp = models.DateTimeField()
    Power = models.DecimalField(max_digits = 8, decimal_places = 3)

    def __str__(self):
        return "Date: " + self.Timestamp.strftime("%m/%d/%y %H:%M:%S") + "  Power: " + str(self.Power)

##Create two seperate classes: EV and Building so we have two separate databases to hold our data 
