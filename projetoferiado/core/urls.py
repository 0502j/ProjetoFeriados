from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.cadastra_feriados_api),
    path('cadastro', views.cadastro, name='cadastro'),
]