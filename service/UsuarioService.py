from persistence import UsuarioPersistence


def administrador_cadastra(servico):
    return UsuarioPersistence.administrador_cadastra(servico)


def suporte_cadastra(servico):
    return UsuarioPersistence.suporte_cadastra(servico)


def atualiza(servico, pk):
    return UsuarioPersistence.atualiza(servico, pk)


def lista_por_empresa_perfil(empresa, perfil):
    return UsuarioPersistence.lista_por_empresa_perfil(empresa, perfil)


def lista_por_perfil(perfil):
    return UsuarioPersistence.lista_por_perfil(perfil)

