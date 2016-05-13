from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/cadastrar_usuario', views.cadastro_usuario),
    url(r'^admin/admin_principal', views.admin_principal),
    url(r'^admin/suporte_principal', views.suporte_princpal),
    url(r'^admin/relatorio', views.relatorio),
    url(r'^suporte/cadastro_admin', views.cadastro_admin),
    url(r'^admin/cadastro_servico', views.cadastro_servico),
    url(r'^suporte/cadastro_estabelecimento', views.cadastro_estabelecimento),
]