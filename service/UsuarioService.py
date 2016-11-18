from persistence import UsuarioPersistence


def administrador_cadastra(usuario):
    return UsuarioPersistence.administrador_cadastra(usuario)


def suporte_cadastra(usuario):
    return UsuarioPersistence.suporte_cadastra(usuario)


def atualiza(servico, pk):
    return UsuarioPersistence.atualiza(servico, pk)


def adiciona_senha(request, pk):
    return UsuarioPersistence.adiciona_senha(request, pk)


def lista_por_empresa_perfil(empresa, perfil):
    return UsuarioPersistence.lista_por_empresa_perfil(empresa, perfil)


def lista_por_perfil(perfil):
    return UsuarioPersistence.lista_por_perfil(perfil)


def usuario_por_id(pk):
    return UsuarioPersistence.usuario_por_id(pk)

