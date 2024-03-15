from django.db import models

class Proxy(models.Model):
# Create your models here.
# ip,port,protocol,country,and uptime
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip}:{self.port}"
    
