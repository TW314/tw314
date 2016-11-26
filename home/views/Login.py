from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service import UsuarioService
from form import LoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

template_name = 'home/login.html'


def login(request):

    guiche = 0
    servico = 0
    fila = 0
    pegar_codigo = 0
    senha = 0

    return render(request, template_name, params(guiche, servico, fila, senha, pegar_codigo))


def params(guiche, servico, fila, senha, pegar_codigo):
    return {"guiche": guiche, "servico": servico, 'fila': fila, 'senha': senha, 'pegar_codigo': pegar_codigo}