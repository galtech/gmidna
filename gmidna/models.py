from django.db import models
from django.forms import ModelForm

# table to store CSV data records
class Flexstar(models.Model):
    patientID = models.CharField(max_length=20)
    twoDBarcode = models.IntegerField(default=0)
    well_position = models.IntegerField(default=0)
    dateImported = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.patientID

# table to store hospital data from XML file
class HospitalData(models.Model):
    patientID = models.CharField(max_length=20)
    barcode = models.CharField(max_length=25)
    dateImported = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.patientID


class FlexStarForm(ModelForm):
    class Meta:
        models = Flexstar
        fields = ['patientID', 'twoDBarcode', 'well_position']

