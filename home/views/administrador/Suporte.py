from django.shortcuts import render, redirect, get_object_or_404, render_to_response


def template(request):
    user = request.session["user"]

    return render(request, 'home/admin/admin_contatar_suporte.html', {"user": user})

