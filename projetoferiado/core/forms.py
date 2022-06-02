from django import forms


class FeriadoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    ano = forms.IntegerField()
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    def clean_dia(self):
            dia = self.cleaned_data['dia']
            if dia < 1 or dia > 30:
                raise TypeError('O dia inserido é inválido')
            return dia