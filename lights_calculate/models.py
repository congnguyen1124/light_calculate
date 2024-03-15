from django.db import models

class Light(models.Model):
    brightness = models.IntegerField()
