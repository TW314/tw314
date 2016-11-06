from pip._vendor import requests

from form.EmpresaForm import EmpresaForm

def busca_por_cnpj(cnpj):
    empresa = requests.get('http://localhost:3000/empresa/' + cnpj).json()
    return empresa