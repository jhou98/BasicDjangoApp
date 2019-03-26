from django.db import models

class powerData(models.Model):
    """
    Class that holds 3 variables
        1. index 
        2. Timestamp: DateTime
        3. Power: Float field
    """
    index = models.AutoField(primary_key=True)
    Timestamp = models.DateTimeField()
    Power = models.FloatField()

    def __str__(self):
        return "Date: " + self.Timestamp.strftime("%m/%d/%y %H:%M:%S") + "  Power: " + str(self.Power)

##Create two seperate classes: EV and Building so we have two separate databases to hold our data 
class EVEnergy(models.Model):
    """
    Class that represents overall EV energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class BuildingEnergy(models.Model):
    """
    Class that represents overall building energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

##Class specific to each EV parkade 
class WestEV(models.Model):
    """
    Class that represents West Parkade energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class RoseEV(models.Model):
    """
    Class that represents Rose Parkade energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class NorthEV(models.Model):
    """
    Class that represents North Parkade energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class HealthEV(models.Model):
    """
    Class that represents Health Sciences Parkade energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class FraserEV(models.Model):
    """
    Class that represents Fraser Parkade energy consumption 
        1. timestamp: Datetime field 
        2. value: Energy consumption
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class carData(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers 
        1. timestamp: Datetime field
        2. totalcars: Total number cars connected to EV chargers
        3. chargedcars: Total number of cars that are fully charged but still connected 
    """
    timestamp = models.DateTimeField(primary_key=True)
    totalcars = models.IntegerField()
    chargedcars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Total Cars: "+str(self.totalcars) + ", Charged Cars: "+str(self.chargedcars)

class buildingData(models.Model):
    """
     Class the represents building data energy 
        1. timestamp: Datetime field
        2. value: Energy consumption 
    Currently not used (waiting for API connection)
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "Timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " Energy: " + str(self.value)

class WestEVFuture(models.Model):
    """
    Class that holds the predicted values for the EV power. 
        1. timestamp: Datetime field
        2. value: Predicted value 
        3. maxerr: Maximum error value  
        4. minerr: Minimum error value 
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()
    maxerr = models.FloatField()
    minerr = models.FloatField()

    def __str__(self):
        return "For future timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " the predicted Energy is " + str(self.value) + \
            " with max/min error of " + str(self.maxerr) + "/" + str(self.minerr)

class buildingEVFuture(models.Model):
    """
    Class that holds the predicted values for the building power. 
        1. timestamp: Datetime field
        2. value: Predicted value 
        3. maxerr: Maximum error value  
        4. minerr: Minimum error value 
    """
    timestamp = models.DateTimeField(primary_key=True)
    value = models.FloatField()
    maxerr = models.FloatField()
    minerr = models.FloatField()

    def __str__(self):
        return "For future timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " the predicted Energy is " + str(self.value) + \
            " with max/min error of " + str(self.maxerr) + "/" + str(self.minerr)

class varDataFuture(models.Model):
    """
    Class that holds the predicted values for the building power. 
        1. timestamp: Datetime field
        2. value: Predicted value 
        3. maxerr: Maximum error value  
        4. minerr: Minimum error value 
    """
    timestamp = models.DateTimeField(primary_key=True)
    totalcars = models.IntegerField()
    chargedcars = models.IntegerField()
    maxerr = models.FloatField()
    minerr = models.FloatField()
    
    def __str__(self):
        return "For future timestamp: " + self.timestamp.strftime("%m/%d/%y %H:%M:%S") + " the predicted Energy is " + str(self.value) + \
            " with max/min error of " + str(self.maxerr) + "/" + str(self.minerr)