from django.urls import path 
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name="contact"),
    path('subjects/', subjects, name="subjects"),
    path('teachers/', teachers, name="teachers"),
    path('managers/', managers, name="managers"),
    path('etabs/', etablissement, name="etabs"),
]