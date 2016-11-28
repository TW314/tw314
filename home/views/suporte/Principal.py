#from django.views.generic import TemplateView
#class IndexView(TemplateView):
#    template_name = "home/suporte/suporte_principal.html"
from django.shortcuts import render, redirect, get_object_or_404, render_to_response


def template(request):
    user = request.session["user"]
    return render(request, 'home/suporte/suporte_principal.html', {"user": user})
