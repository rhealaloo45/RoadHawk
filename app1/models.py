from django.db import models

# Create your models here.
class potData(models.Model):
    ultra = models.FloatField(max_length=15)
    gyro_x = models.FloatField(max_length=15)
    gyro_y = models.FloatField(max_length=15)
    gyro_z = models.FloatField(max_length=15)
    gps_time = models.CharField(max_length=15)
    gps_lat = models.FloatField(max_length=15)
    gps_long = models.FloatField(max_length=15)
    
    def __str__(self):
        return self.ultra
    