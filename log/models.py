from django.db import models

class Log(models.Model):
    mesaid = models.CharField(max_length=7)
    barcode = models.TextField(max_length=10)
    wake = models.DateField()
