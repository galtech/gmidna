from django import forms
import csv
from django.utils import timezone


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    def parseFile(self, csvFile = None, xmlFile = None):
        if(csvFile != None):
            with open(csvFile, mode='r') as cf:
                reader = csv.reader(cf, delimiter=',')
                lineCount = 1 # start at first row of data.
                for row in reader:
                    if lineCount > 0:
                        created = Flexstar.objects.get_or_create(
                            patientID=row[0],
                            twoDBarcode=row[1],
                            well_position=row[2],
                            dateImported=timezone.now()
                        )
                        lineCount+=1

