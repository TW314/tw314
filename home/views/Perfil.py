from django.shortcuts import render, redirect
from service.UsuarioService import usuario_por_id


def template(request, pk):
    perfil = usuario_por_id(pk)
    user = request.session["user"]

    return render(request, 'home/perfil.html', {"perfil": perfil, "user": user})




