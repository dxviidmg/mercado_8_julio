from django.urls import path

from negocios.views import NegocioListView

urlpatterns = [
    path('', NegocioListView.as_view(), name='negocio-list'),
]