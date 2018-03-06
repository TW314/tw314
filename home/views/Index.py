from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from form.ContatarForm import ContatarForm
from django.views.decorators.http import require_POST
from django.core.mail import send_mail, send_mass_mail
from django.urls import reverse


# Index
def index(request):
    form = ContatarForm()

    if request.method == "POST":
        contatar(request)
        return redirect(reverse('login'))

    return render(request, 'home/index.html', params(form))


def params(form):
    return {'form': form}


@require_POST
def contatar(request):

    # contatar = (
    #     (
    #         '[Contato] TW314 - Dúvida de ' + request.nome,
    #         'TeamTW, há um visitante com dúvidas.' +
    #         'NOME: ' + request.nome +
    #         'E-MAIL: ' + request.email +
    #         'ASSUNTO: ' + request.assunto +
    #         'MENSAGEM: ' + request.mensagem,
    #         'contatotw314@gmail.com',
    #         ['contatotw314@gmail.com', 'haluanedecassia@gmail.com']
    #     ),
    #     (
    #         '[Contato] TW314 - Dúvida',
    #         'Obrigado por se interessar no TW314! <3. A equipe responderá em breve.' +
    #         'HORA DO CONTATO: ' +
    #         'DATA DO CONTATO' +
    #         'Você está recebendo esse e-mail porque essa conta foi usada para receber ' +
    #         'perguntas sobre o sistema. Caso já tenha sido respondido ou não ter enviado, ' +
    #         'ignore esse e-mail.',
    #         'contatotw314@gmail.com',
    #         [request.email]
    #     )
    # )
    #
    # send_mass_mail(contatar, fail_silently=False)

    send_mail(
        '[Contato] TW314 - Dúvida de ' + 'request.cleaned_data[\'nome\']',
        'TeamTW, há um visitante com dúvidas.' +
        'NOME: ' + 'request.cleaned_data[\'nome\']' +
        'E-MAIL: ' + 'request.cleaned_data[\'email\']' +
        'ASSUNTO: ' + 'request.cleaned_data[\'assunto\']' +
        'MENSAGEM: ' + 'request.cleaned_data[\'mensagem\']',
        'contatotw314@gmail.com',
        ['contatotw314@gmail.com', 'haluanedecassia@gmail.com'],
        fail_silently=False,
        )
    return redirect(reverse('/login'))
