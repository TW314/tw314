from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service.ServicoService import servico_por_id


def template(request):
    guiche = request.session["guiche"]
    servico = servico_por_id(request.session["servico"])
    return render(request, 'home/funcionario/funcionario_principal.html', {"guiche": guiche, "servico": servico})

