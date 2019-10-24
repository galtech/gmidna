from django import forms
import csv
import xml.etree.ElementTree as ET
from django.utils import timezone


class UploadCSVFileForm(forms.Form):
    file = forms.FileField()
    #title = forms.CharField(max_length=50)

    def parseCSVFile(self, csvFile = None):
        data = list()
        if(csvFile != None):
            with open(csvFile, mode='r') as cf:
                cr = csv.reader(cf, delimiter=',')
                next(cr)
                data = list(cr)
                return data

class UploadXMLFileForm(forms.Form):
    file = forms.FileField()
    #title = forms.CharField(max_length=50)

    def parseXMLFile(self, xmlFile):
        root = ET.parse(xmlFile).getroot()
        results = root.findall('sample')
        for sample in results:
            patientID = sample.find('patient-id')
            barcode = sample.find('barcode')
            if patientID is not None:
                hospdata = {patientID.text:barcode.text}
                return hospdata
