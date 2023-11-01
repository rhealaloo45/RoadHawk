from django.db import models
from django.utils import timezone

# Create your models here.
class potData(models.Model):
    ultra = models.FloatField(max_length=15)
    gyro_x = models.FloatField(max_length=15)
    gyro_y = models.FloatField(max_length=15)
    gyro_z = models.FloatField(max_length=15)
    # gps_date = models.DateField(default=timezone.now)
    gps_lat = models.FloatField(max_length=15)
    gps_long = models.FloatField(max_length=15)
    
    def __str__(self):
        return "Pothole detected"
    