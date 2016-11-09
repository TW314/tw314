from django.conf.urls import url
from .views import suporte
from .views import administrador
from .views import funcionario

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^login', views.login),
    # administrador
    url(r'^administrador/cadastrar_usuario', administrador.CadastroUsuario.template),
    url(r'^administrador/principal', administrador.Principal.template),
    url(r'^administrador/cadastro_servico', administrador.CadastroServico.template),
    url(r'^administrador/relatorio', administrador.Relatorio.template),
    url(r'^administrador/suporte', administrador.Suporte.template),
    url(r'^administrador/sobre', administrador.Sobre.template),
    # suporte
    url(r'^suporte/principal', suporte.Principal.template),
    url(r'^suporte/cadastro_admin', suporte.CadastroUsuario.template),
    url(r'^suporte/cadastro/empresa', suporte.CadastroEstabelecimento.template),
    url(r'^suporte/atendimento', suporte.Atendimento.template),
    url(r'^suporte/cadastro/servico', suporte.CadastroServico.template),
    url(r'^suporte/cadastro/ramo', suporte.CadastroRamoAtividade.template),
    url(r'^suporte/editar/ramo/(?P<pk>[0-9]+)/$', suporte.AtualizaRamoAtividade.template),
    url(r'^suporte/editar/servico/(?P<pk>[0-9]+)/$', suporte.AtualizaServico.template),
    url(r'^suporte/editar/empresa/(?P<pk>[0-9]+)/$', suporte.AtualizaEstabelecimento.template, name='editar_empresa'),
    # funcionario
    url(r'^funcionario/principal', funcionario.Principal.template),
    url(r'^funcionario/relatorio', funcionario.Relatorio.template),
    url(r'^funcionario/suporte', funcionario.Suporte.template),
    url(r'^funcionario/sobre', funcionario.Sobre.template),

    #url(r'^teste', views.demo_chart),
]
