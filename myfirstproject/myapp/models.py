from django.db import models

# Create your models here.
class Feature(models.Model):
    # id: int ko can vi da tu dong load phan nay ket noi voi uan ly database
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
     