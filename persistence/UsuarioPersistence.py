# coding=utf-8
from pip._vendor import requests
from form.UsuarioForm import UsuarioForm
from form.SenhaForm import SenhaForm
from form.LoginForm import LoginForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import bcrypt


def administrador_cadastra(request, usuario):
    now = datetime.now()
    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']
        empresa = request.session["user"]["empresa"]["id"]
        data = administrador_monta_json(nome, email, status_ativacao, empresa)
        send_mail(
            'Bem-vindo ao time TW314',
            'Olá, ' + nome + '! Esse e-mail foi cadastrado em nosso sistema em ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' às ' + str(now.hour) + ':' + str(now.minute) + 'hrs. Aguarde novo contato para cadastrar sua senha. Se acredita que houve um engano, por favor, entre em contado pelo e-mail contatotw314@gmail.com . Att, Time TW314',
            'contatotw314@gmail.com',
            [email],
            fail_silently=False,
            )
        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "<h3>Campos de Usuario nao preenchidos corretamente</h3>"

    return form


def administrador_atualiza(usuario_novo, usuario, pk):
    form = UsuarioForm(usuario_novo)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = usuario['status_ativacao']

        data = administrador_monta_json(nome, email, status_ativacao)

        try:
            form = requests.put('http://localhost:3000/usuario/' + pk, json=data)
        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Servico nao preenchidos corretamente"

    return form


def suporte_cadastra(usuario):
    now = datetime.now()
    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']
        empresa = form.cleaned_data['empresa']

        data = suporte_monta_json(nome, email, empresa, status_ativacao)
        send_mail(
            'Bem-vindo ao time TW314',
            'Olá, ' + nome + '! Esse e-mail foi cadastrado em nosso sistema em ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' às ' + str(now.hour) + ':' + str(now.minute) + 'hrs. Aguarde novo contato para cadastrar sua senha. Se acredita que houve um engano, por favor, entre em contado pelo e-mail contatotw314@gmail.com . Att, Time TW314',
            'contatotw314@gmail.com',
            [email],
            fail_silently=False,
            )
        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "<h3>Campos de Usuario nao preenchidos corretamente</h3>"

    return form


def suporte_atualiza(usuario_novo, usuario, pk):
    form = UsuarioForm(usuario_novo)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = usuario['status_ativacao']
        empresa = form.cleaned_data['empresa']

        data = suporte_monta_json(nome, email, empresa, status_ativacao)

        try:
            form = requests.put('http://localhost:3000/usuario/' + pk, json=data)
        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        return "<h3>Campos de Servico nao preenchidos corretamente</h3>"

    return form


def adiciona_senha(usuario_novo, pk):
    form = SenhaForm(usuario_novo)

    if form.is_valid():
        senha = form.cleaned_data['senha'].encode()
        senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt())
        print(senha_hash.decode)
        try:
            form = requests.put('http://localhost:3000/usuario/' + str(pk), json={'senha': senha_hash.decode("utf8")})

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"

    return form


def lista_por_empresa_perfil(empresa, perfil):
    usuario = requests.get('http://localhost:3000/usuario/empresa/' + str(empresa) + "&" + str(perfil)).json()
    return usuario


def lista_por_perfil(perfil):
    return requests.get('http://localhost:3000/usuario/perfil/' + str(perfil)).json()


def suporte_monta_json(nome, email, empresa, status_ativacao, data_inativacao=None):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao,
            'data_inativacao': data_inativacao,'empresaId': empresa, 'perfilId': 2}
    return data


def administrador_monta_json(nome, email, status_ativacao, empresaId, data_inativacao=None):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao,
            'data_inativacao': data_inativacao, 'perfilId': 3, 'empresaId': empresaId}

    return data


def usuario_por_id(pk):
    usuario = requests.get('http://localhost:3000/usuario/'+str(pk)).json()
    return usuario


def usuario_por_email(email):
    usuario = requests.get('http://localhost:3000/login/'+str(email)).json()
    return usuario

t = 0


def loga(request, login):
    form = LoginForm(login)
    global t
    t += 1
    if t <= 3:
        print(t)
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            user = usuario_por_email(email)
            senha_user = user["senha"]
            if user and type(user) != int:
                if bcrypt.checkpw(senha.encode(), senha_user.encode()):
                    usuario = usuario_por_id(user["id"])
                    request.session["user"] = usuario
                    if user["perfil"]["id"] == 1:
                        request.session.set_expiry(600)
                    if user["perfil"]["id"] == 2:
                        request.session.set_expiry(300)
                    if user["perfil"]["id"] == 3:
                        request.session.set_expiry(0)
                    t = 0
                else:
                    return HttpResponse("OPS! Senha incorreta, tente novamente")
            elif type(user) == int:
                return HttpResponse("404")
            else:
                return HttpResponse("OPS! Parece que esse usuário não existe em nosso sistema. Contate o seu administrador")
        else:
            return form.errors
    else:
        return HttpResponse("Parece que você tentou muito entrar! Contate o admnistrador")
