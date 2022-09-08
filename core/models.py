from email.policy import default

from django.db import models


# Create your models here.
class IncomingRequest(models.Model):
    ipware = models.JSONField(default=dict)
    ipinfo = models.JSONField(default=dict)
    latitude = models.CharField(max_length=40, null=True, blank=True)
    longitude = models.FloatField(max_length=40, null=True, blank=True)
    track_date = models.DateTimeField(auto_now_add=True)
