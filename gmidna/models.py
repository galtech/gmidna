from django.db import models
from django.forms import ModelForm

class Flexstar(models.Model):
    patientID = models.IntegerField(default=0)
    twoDBarcode = models.IntegerField(default=0)
    well_position = models.IntegerField(default=0)
    dateImported = models.DateTimeField('date imported')

class HospitalData(models.Model):
    patientID = models.IntegerField(default=0)
    barcode = models.CharField(max_length=25)
    dateImported = models.DateTimeField('date imported')

