from django.shortcuts import render
from django.views.generic.list import ListView
from negocios.models import Negocio

class NegocioListView(ListView):
    model = Negocio
