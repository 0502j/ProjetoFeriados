from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado',max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    ano = models.IntegerField(default=2022)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)
        
def __str__(self):
    return self.nome


class FeriadoModelApi(models.Model):
    nome = models.CharField('feriado', max_length=200)
    data = models.DateField('data')

    def __str__(self):
        return self.nome