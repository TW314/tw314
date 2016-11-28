from django.shortcuts import render
from service import EmpresaServicoService
from service import ServicoService
from form.EmpresaServicoForm import EmpresaServicoForm
from django.views.decorators.http import require_POST

# rel_emp_svc == Objeto da tabela de relacionamento entre empresa e servico
template_name = 'home/admin/admin_insere_servico.html'


def template(request):
    user = request.session["user"]

    form = EmpresaServicoForm()
    if request.method == "POST":
        cadastra(request)

    servicos = servicos_listar()

    rel_emp_svc = rel_emp_svc_listar(request)
    return render(request, template_name, params(form, servicos, rel_emp_svc, user))


@require_POST
def cadastra(rel_emp_svc):
    EmpresaServicoService.cadastra(rel_emp_svc.POST)


def servicos_listar():
    return ServicoService.lista()


def rel_emp_svc_listar(request):
    empresa = 1
    return EmpresaServicoService.lista(empresa)


def params(form, servicos, rel_emp_svc, user):
    return {"form": form, "servicos": servicos, "rel_emp_svc": rel_emp_svc, "user": user}
