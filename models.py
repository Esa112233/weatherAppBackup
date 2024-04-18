from django.db import models
# make it so that all data is recieved, if one value is missing, raise an error and show where this error was
# Create your models here.
class WeatherInfo(models.Model):
    metStationId = models.IntegerField()
    dataCollectionType = models.CharField(max_length=50)
    dateTaken = models.DateTimeField(primary_key=True)
    windSpeed = models.DecimalField(decimal_places=2, max_digits=10)
    windDirection = models.DecimalField(decimal_places=2, max_digits=10)
    temperature = models.DecimalField(decimal_places=2, max_digits=10)
    solarRadiation = models.DecimalField(decimal_places=3, max_digits=10)
    humidity = models.DecimalField(decimal_places=2, max_digits=10)
    uComponent = models.DecimalField(decimal_places=2, max_digits=10)
    vComponent = models.DecimalField(decimal_places=2, max_digits=10)
    sigmaTheta = models.DecimalField(decimal_places=2, max_digits=10)
    hStability = models.IntegerField()
    vStability = models.IntegerField()
    rainfall = models.IntegerField()
    scalarWindSpeed = models.DecimalField(decimal_places=2, max_digits=10)
    scalarWindDirection = models.DecimalField(decimal_places=2, max_digits=10)
    sigmaWindSpeed = models.IntegerField()
    pressure = models.DecimalField(decimal_places=2, max_digits=10)
    wComponent = models.IntegerField()
    sigmaPhi = models.IntegerField()
    maxWindSpeed = models.DecimalField(decimal_places=2, max_digits=10)
    feelsLike = models.DecimalField(decimal_places=2, max_digits=10)
    corridorHalfAngle = models.DecimalField(decimal_places=2, max_digits=10)
    solarRadiationCalculated = models.IntegerField()
    windDirectionText = models.IntegerField()
    rainRate = models.DecimalField(decimal_places=2, max_digits=10)
    rainRateEstimated = models.DecimalField(decimal_places=2, max_digits=10)
    
    # Remember to do condo activate Test or something
    
class WeatherInfoRequired(models.Model):
    maxWindSpeed = models.DecimalField(decimal_places=2, max_digits=10, null=True),
    feelsLike = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    temperature = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    humidity = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    pressure = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    rainfall = models.IntegerField(null=True)
    rainRate = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    solarRadiation = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    hStability = models.IntegerField(null=True)
    vStability = models.IntegerField(null=True)
    
