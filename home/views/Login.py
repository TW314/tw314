from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service import UsuarioService
from form.LoginForm import LoginForm
import bcrypt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

template_name = 'home/login.html'


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = logar(request)
        if request.session["user"]["perfil"]["id"] == 1:
            return HttpResponseRedirect(reverse('suporte_principal'))
        if request.session["user"]["perfil"]["id"] == 2:
            return HttpResponseRedirect(reverse('admin_principal'))
        if request.session["user"]["perfil"]["id"] == 3:
            return HttpResponseRedirect(reverse('funcionario_principal'))
    else:
        print("teu cu request nao e post")

    return render(request, template_name, params(form))


@require_POST
def logar(request):
    return UsuarioService.loga(request, request.POST)


def params(form, usuario=None):
    return {"form": form, "usuario": usuario}
