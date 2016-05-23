from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    #url(r'^sobre', views.sobre),
    # admin
    url(r'^admin/cadastrar_usuario', views.admin_cadastro_usuario),
    url(r'^admin/principal', views.admin_principal),
    url(r'^admin/cadastro_servico', views.admin_cadastro_servico),
    url(r'^admin/relatorio', views.admin_relatorio),
    url(r'^admin/suporte', views.admin_suporte),
    url(r'^admin/sobre', views.admin_sobre),
    # suporte
    url(r'^suporte/principal', views.suporte_princpal),
    url(r'^suporte/cadastro_admin', views.suporte_cadastro_admin),
    url(r'^suporte/cadastro_estabelecimento', views.suporte_cadastro_estabelecimento),
    url(r'^suporte/atendimento', views.suporte_atendimento),
    # funcionario
    url(r'^funcionario/principal', views.funcionario_principal),
    url(r'^funcionario/relatorio', views.funcionario_relatorio),
    url(r'^funcionario/suporte', views.funcionario_suporte),
    url(r'^funcionario/sobre', views.funcionario_sobre),

    url(r'^teste', views.demo_chart),
]