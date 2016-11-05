from django.shortcuts import render, redirect, get_object_or_404, render_to_response


def template(request):
    return render(request, 'home/suporte/suporte_atendimento.html', {})

