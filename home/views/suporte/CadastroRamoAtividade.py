from django.shortcuts import render
from service import RamoAtividadeService
from form.RamoForm import RamoForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

template_name = 'home/suporte/suporte_cadastro_ramo.html'


def template(request):
    user = request.session["user"]
    if request.method == "POST":
        cadastra(request)

    form = RamoForm()
    ramos = RamoAtividadeService.lista()

    return render(request, template_name, params(form, ramos, user))


@require_POST
def cadastra(ramo_atividade):
    RamoAtividadeService.cadastra(ramo_atividade.POST)


def params(form, ramos, user):
    return {'form': form, 'ramos': ramos, "user": user}


def listing(request):
    ramos_list = RamoAtividadeService.lista()
    paginator = Paginator(ramos_list, 1)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        ramos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ramos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ramos = paginator.page(paginator.num_pages)

    return render(request, template_name, {'ramos': ramos, 'page': page})
