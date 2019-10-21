from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm

from .forms import parseFile

def index(request):
    dataCapture = """
        <style>html{font-family: sans-serif;}</style>
        <h2>Data Import</h2>
    
        <form method="POST" enctype="multipart/form-data" name="dnaForm">    
            <input type='file' placeholder='CSV import'>
            <input type="submit" value="Upload blood sample DNA"><br><br>
        </form>
        
        <form method="POST" enctype="multipart/form-data" name="bloodForm">
            <input type='file' placeholder='XML import'>
            <input type="submit" value="Upload blood samples">
        </form>
    """
    return HttpResponse(dataCapture)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            parseFile(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
