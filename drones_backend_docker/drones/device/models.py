from django.db import models

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    altitude = models.FloatField()
    dist_id = models.CharField(max_length=12)
    video_url = models.URLField(blank=True, null=True)  
    status = models.CharField(max_length=15)

    
    class Meta:
        db_table = 'drones'

class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=45)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    district = models.IntegerField()

    class Meta:
        db_table = 'incidents'