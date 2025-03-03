from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("NOM_details",views.NOM_details, name='NOM_details'),
    path("Femto_small_cells",views.Femto_small_cells, name='Femto_small_cells')
]