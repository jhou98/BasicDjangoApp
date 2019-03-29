from django.db import models

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

# class for building (can make more per building)
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

class buildingFuture(models.Model):
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

# Class for vehicle data (can make more for each parkade)
class chargedCarsData(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsData(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
        3. maxerr: Maximum error value  
        4. minerr: Minimum error value 
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.FloatField()
    maxerr = models.FloatField()
    minerr = models.FloatField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars) + \
            " with max/min error of " + str(self.maxerr) + "/" + str(self.minerr)

class chargingCarsFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging
        3. maxerr: Maximum error value  
        4. minerr: Minimum error value 
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.FloatField()
    maxerr = models.FloatField()
    minerr = models.FloatField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars) + \
            " with max/min error of " + str(self.maxerr) + "/" + str(self.minerr)
