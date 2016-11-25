from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from form.GuicheServicoForm import GuicheServicoForm
from django.core.urlresolvers import reverse
from service.EmpresaServicoService import lista


def template(request):
    form = GuicheServicoForm(request.POST)
    servicos = lista(1)
    guiches = [x*1 for x in range(1, 6)]

    if request.method == "POST":
        if form.is_valid():
            request.session['guiche'] = form.cleaned_data['guiche']
            request.session['servico'] = form.cleaned_data['servico']
            print(request.session['guiche'] + "-" + request.session['servico'])
            return redirect(reverse('funcionario_principal'))

    return render(request, 'home/funcionario/funcionario_escolher_guiche_servico.html', {'form': form, 'servicos': servicos, 'guiches': guiches})
