from django.urls import path
from .views import mymodel_create_view

urlpatterns = [
    path('mymodel/create/', mymodel_create_view, name='mymodel_create'),  # URL to access the form
    # other URL patterns...
]