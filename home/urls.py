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
    url(r'^suporte/cadastro_estabelecimento', suporte.CadastroEstabelecimento.template),
    url(r'^suporte/atendimento', suporte.Atendimento.template),
    url(r'^suporte/cadastro_servico', suporte.CadastroServico.template),
    url(r'^suporte/cadastro_ramos', suporte.CadastroRamoAtividade.template),
    # url(r'^suporte/editar_status/(?P<pk>[0-9]+)/$', views.suporte_editar_status),
    # url(r'^suporte/editar_ramos/(?P<pk>[0-9]+)/$', views.suporte_editar_ramos),
    # url(r'^suporte/editar_servicos/(?P<pk>[0-9]+)/$', views.suporte_editar_servicos),
    # funcionario
    url(r'^funcionario/principal', funcionario.Principal.template),
    url(r'^funcionario/relatorio', funcionario.Relatorio.template),
    url(r'^funcionario/suporte', funcionario.Suporte.template),
    url(r'^funcionario/sobre', funcionario.Sobre.template),

    #url(r'^teste', views.demo_chart),
]
