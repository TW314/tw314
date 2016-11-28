from django.shortcuts import render, redirect, get_object_or_404, render_to_response


# Index
def suporte(request):
    user = request.session["user"]
    return render(request, 'master_suporte.html', {"user": user})


def admin(request):
    user = request.session["user"]
    return render(request, 'master_admin.html', {"user": user})


def func(request):
    user = request.session["user"]
    return render(request, 'master_funcionario.html', {"user": user})
