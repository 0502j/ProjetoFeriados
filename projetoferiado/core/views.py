from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

from core.forms import FeriadoForm
from .models import FeriadoModel
from .models import FeriadoModelApi
from django.db.models import CharField
from django.db.models.functions import Length
from .FeriadosAPI import FeriadosAPI

def index(request):

    hoje = date.today()

    if FeriadoModel.objects.filter(ano=hoje.year, mes=hoje.month, dia=hoje.day).exists():
        contexto = {
            'ehferiado': True,
        }
    else:
        contexto = {
            'ehferiado': False,
        }
    return render(request, 'index.html', contexto)


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'formulario': FeriadoForm()})
    else:
        formulario = FeriadoForm(request.POST)
        if formulario.is_valid():
            dados = formulario.cleaned_data
            FeriadoModel.objects.create(**dados)
            contexto = {'feriado': dados.get('nome')}
            return render(request, 'cadastro_ok.html', contexto)
        else:
            contexto = {'formulario': formulario}
            return render(request, 'cadastro.html', contexto)


def cadastra_feriados_api(request):
    api = FeriadosAPI(2022)

    for feriado in api.feriados:
        nome, data = feriado
        cadastro = FeriadoModelApi(nome=nome, data=data)
        cadastro.save()

    return HttpResponse('')
