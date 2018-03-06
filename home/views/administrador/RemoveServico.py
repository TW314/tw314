from django.shortcuts import render, redirect
from service import EmpresaService
from django.urls import reverse
from pip._vendor import requests


# rel_emp_svc == Objeto da tabela de relacionamento entre empresa e servico


def remove_servico(request, pk):
    return requests.delete('http://localhost:3000/servicos_empresa/1/' + str(pk))
