from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from .forms import UploadFileForm
from gmidna.models import Flexstar
from .forms import UploadCSVFileForm, UploadXMLFileForm

def index(request):
    dataCapture = """
        Welcome to the data processing app
        <br><br>
        <a href="uploadcsv">Click to upload CSV data</a>
        <br><br>
        <a href="uploadxml">Click to upload XML data</a>
        <br><br>
        <a href="dataview">Click to view sample data</a>        
        """
    return HttpResponse(dataCapture)

def viewdata(request):
    patientList = Flexstar.objects.select_related().all()
    return render(request, 'viewdata.html', { 'data': patientList})

def get_csv(request):
    if request.method == 'POST':
        form = UploadCSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.parseCSVFile(form.cleaned_data)
            return HttpResponse('Thank you. Your CSV file has been uploaded') # TODO: change this to a redirect to data display page
    else:
        form = UploadCSVFileForm()

    return render(request, 'csvupload.html', { 'form': form})

def get_xml(request):
    if request.method == 'POST':
        form = UploadXMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.parseXMLFile(form.cleaned_data)
            return HttpResponse('Thank you. Your XML file has been uploaded') # TODO: change this to a redirect to data display page
    else:
        form = UploadXMLFileForm()

    return render(request, 'xmlupload.html', { 'form': form})
