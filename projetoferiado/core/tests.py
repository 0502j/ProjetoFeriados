from email import message
from http import HTTPStatus
from django.test import TestCase
from .FeriadosAPI import FeriadosAPI

# Create your tests here.
class FormTest(TestCase):
    def setUp(self):
        self.mockedData = {'nome': 'Teste', 'dia': '01', 'mes':'06', 'ano': '2022'}
    def testPost(self):
        res = self.client.post('/cadastro/', data=self.mockedData)

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertContains(res, 'cadastrado com sucesso!')

class FeriadoApiTest(TestCase):
    def test_instanciar_objeto(self):
        objeto = FeriadosAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadosAPI(2023)
        message = 'Feriados de 2023'
        assert str(objeto) == message
        assert repr(objeto) == message

    def test_str_repr2(self):
        objeto = FeriadosAPI(2022)
        message = 'Feriados de 2022'
        assert str(objeto) == message
        assert repr(objeto) == message

    def test_properties(self):
        objeto = FeriadosAPI(2022)
        assert objeto.ano == '2022'