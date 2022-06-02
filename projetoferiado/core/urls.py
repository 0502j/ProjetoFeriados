from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro, name='novo_feriado'),

]