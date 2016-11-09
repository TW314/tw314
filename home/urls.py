from django.conf.urls import url
from .views import suporte
from .views import administrador
from .views import funcionario

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^login', views.login),
    # administrador
    url(r'^administrador/cadastrar_usuario', administrador.CadastroUsuario.template, name='cadastrar_usuario'),
    url(r'^administrador/principal', administrador.Principal.template, name='admin_principal'),
    url(r'^administrador/cadastro_servico', administrador.CadastroServico.template, name='add_servico'),
    url(r'^administrador/relatorio', administrador.Relatorio.template, name='admin_relatorio'),
    url(r'^administrador/suporte', administrador.Suporte.template, name='admin_suporte'),
    url(r'^administrador/sobre', administrador.Sobre.template, name='admin_sobre'),
    # suporte
    url(r'^suporte/principal', suporte.Principal.template, name='suporte_principal'),
    url(r'^suporte/cadastro_admin', suporte.CadastroUsuario.template, name='cadastrar_admin'),
    url(r'^suporte/cadastro/empresa', suporte.CadastroEstabelecimento.template, name='cadastrar_empresa'),
    url(r'^suporte/atendimento', suporte.Atendimento.template, name='atendimento_suporte'),
    url(r'^suporte/cadastro/servico', suporte.CadastroServico.template, name='cadastrar_servico'),
    url(r'^suporte/cadastro/ramo', suporte.CadastroRamoAtividade.template, name='cadastrar_ramo'),
    url(r'^suporte/editar/ramo/(?P<pk>[0-9]+)/$', suporte.AtualizaRamoAtividade.template, name='editar_ramo'),
    url(r'^suporte/editar/servico/(?P<pk>[0-9]+)/$', suporte.AtualizaServico.template, name='editar_servico'),
    url(r'^suporte/editar/empresa/(?P<pk>[0-9]+)/$', suporte.AtualizaEstabelecimento.template, name='editar_empresa'),
    # funcionario
    url(r'^funcionario/principal', funcionario.Principal.template, name='funcionario_principal'),
    url(r'^funcionario/relatorio', funcionario.Relatorio.template, name='funcionario_relatorio'),
    url(r'^funcionario/suporte', funcionario.Suporte.template, name='funcionario_suporte'),
    url(r'^funcionario/sobre', funcionario.Sobre.template, name='funcionario_sobre'),
    # url(r'^teste', views.demo_chart),
]
