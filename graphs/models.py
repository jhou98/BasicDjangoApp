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
    Class that holds the predicted values for the EV power for West Parkade. 
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

class RoseEVFuture(models.Model):
    """
    Class that holds the predicted values for the EV power for Rose Parkade. 
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

class NorthEVFuture(models.Model):
    """
    Class that holds the predicted values for the EV power for North Parkade. 
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

class HealthEVFuture(models.Model):
    """
    Class that holds the predicted values for the EV power for Health Parkade. 
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

class FraserEVFuture(models.Model):
    """
    Class that holds the predicted values for the EV power for Fraser Parkade. 
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
class buildingWest(models.Model):
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

class buildingWestFuture(models.Model):
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

class buildingRose(models.Model):
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

class buildingRoseFuture(models.Model):
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

class buildingHealth(models.Model):
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

class buildingHealthFuture(models.Model):
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

class buildingFraser(models.Model):
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

class buildingFraserFuture(models.Model):
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

class buildingNorth(models.Model):
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

class buildingNorthFuture(models.Model):
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
class chargedCarsWest(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at West Parkade. 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsWest(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at West Parkade.
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsWestFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at West Parkade. 
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

class chargingCarsWestFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at West Parkade.
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

class chargedCarsRose(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Rose Parkade. 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsRose(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Rose Parkade.
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsRoseFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Rose Parkade. 
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

class chargingCarsRoseFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Rose Parkade.
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

class chargedCarsHealth(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Health Parkade. 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsHealth(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Health Parkade.
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsHealthFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Health Parkade. 
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

class chargingCarsHealthFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Health Parkade.
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

class chargedCarsFraser(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Fraser Parkade. 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsFraser(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at Fraser Parkade.
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsFraserFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Fraser Parkade. 
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

class chargingCarsFraserFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at Fraser Parkade.
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

class chargedCarsNorth(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at North Parkade. 
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and done charging (charged)
    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Charged Cars: "+str(self.cars)

class chargingCarsNorth(models.Model):
    """
    Class the represents cars within the lot that are connected to EV chargers at North Parkade.
        1. timestamp: Datetime field
        2. cars: Number of cars that are connected and still charging

    """
    timestamp = models.DateTimeField(primary_key=True)
    cars = models.IntegerField()

    def __str__(self):
        return "Timestamp: " +  self.timestamp.strftime("%m/%d/%y %H:%M:%S") + "Cars Charging: "+str(self.cars)

class chargedCarsNorthFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at North Parkade. 
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

class chargingCarsNorthFuture(models.Model):
    """
    Class the represents predicted value of cars in a lot that are connected to EV chargers at North Parkade.
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


