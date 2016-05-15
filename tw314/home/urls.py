from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
    #admin
    url(r'^admin/cadastrar_usuario', views.cadastro_usuario),
    url(r'^admin/admin_principal', views.admin_principal),
    url(r'^admin/cadastro_servico', views.cadastro_servico),
    url(r'^admin/relatorio', views.relatorio),
    #suporte
    url(r'^suporte/suporte_principal', views.suporte_princpal),
    url(r'^suporte/cadastro_admin', views.cadastro_admin),
    url(r'^suporte/cadastro_estabelecimento', views.cadastro_estabelecimento),
    url(r'^suporte/suporte_atendimento', views.suporte_atendimento),

    #funcionario
    url(r'funcionario/funcionario_princpal', views.funcionario_principal),

    url(r'^teste', views.demo_chart),


]