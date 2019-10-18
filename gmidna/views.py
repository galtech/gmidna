from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dataCapture = """
        <style>html{font-family: sans-serif;}</style>
        <h2>Data Import</h2>
    
        <input type='file' placeholder='CSV import'>
        <button>Upload blood sample DNA</button><br><br>
        <input type='file' placeholder='XML import'>
        <button>Upload blood samples</button>
    """
    return HttpResponse(dataCapture)

