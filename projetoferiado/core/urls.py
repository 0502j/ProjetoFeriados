from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastra', views.cadastra_feriados_api),
    path('cadastro', views.cadastro, name='novo_feriado'),
]