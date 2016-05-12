from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/cadastrar_usuario', views.cadastro_usuario),
    url(r'^admin/admin_principal', views.admin_principal),
    url(r'^admin/suporte_principal', views.suporte_princpal),
    url(r'^admin/relatorio', views.relatorio),
    url(r'^suporte/cadastro_admin', views.cadastro_admin),
]