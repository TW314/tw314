from django.shortcuts import render, redirect
from service import UsuarioService
from form.SenhaForm import SenhaForm
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

template_name = 'home/suporte/suporte_adicionar_senha.html'


def template(request, pk):

    form = SenhaForm()

    if request.method == "POST":
        adiciona_senha(request, pk)
        return redirect(reverse('login'))

    return render(request, template_name, params(form))


@require_POST
def adiciona_senha(request, pk):
    UsuarioService.adiciona_senha(request.POST, pk)


def params(form):
    return {'form': form}


def enviar_email(request, pk):
    usuario = UsuarioService.usuario_por_id(pk)
    send_mail(
        'Nova Senha em TW314',
        'Olá, ' + usuario['nome'] + '! Para continuar e acessar sua conta no sistema TW314, acesso o link http://localhost:8000' + str(reverse('adiciona_senha', args=[usuario['id']])) + ' e cadastre sua nova senha. Se acredita que houve um engano, por favor, entre em contado pelo e-mail contato@tw314.com.br. Att, Time TW314',
        'contatotw314@gmail.com',
        [usuario['email']],
        fail_silently=False,
    )
    return redirect(reverse('cadastrar_admin'))
