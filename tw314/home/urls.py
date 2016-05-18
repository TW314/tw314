from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    # admin
    url(r'^admin/admin_cadastrar_usuario', views.admin_cadastro_usuario),
    url(r'^admin/admin_principal', views.admin_principal),
    url(r'^admin/admin_cadastro_servico', views.admin_cadastro_servico),
    url(r'^admin/admin_relatorio', views.admin_relatorio),
    # suporte
    url(r'^suporte/suporte_principal', views.suporte_princpal),
    url(r'^suporte/suporte_cadastro_admin', views.suporte_cadastro_admin),
    url(r'^suporte/suporte_cadastro_estabelecimento', views.suporte_cadastro_estabelecimento),
    url(r'^suporte/suporte_atendimento', views.suporte_atendimento),
    # funcionario
    url(r'^funcionario/funcionario_princpal', views.funcionario_principal),
    url(r'^funcionario/funcionario_sobre', views.sobre),
    url(r'^funcionario/funcionario_relatorio', views.funcionario_relatorio),

    url(r'^teste', views.demo_chart),

]
