# seismic_app/urls.py
from django.urls import path
from .views import seismic_data_view

urlpatterns = [
    path('seismic-data/', seismic_data_view, name='seismic_data'),
]
