from pip._vendor import requests

from form.EmpresaForm import EmpresaForm

def busca_por_cnpj(empresa):
    servico = requests.get('http://localhost:3000/servico/' + empresa).json()
    return servico