from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadcsv', views.get_csv, name='get_csv'),
    path('uploadxml', views.get_xml, name='get_xml'),
    path('dataview', views.viewdata, name='viewdata'),
]