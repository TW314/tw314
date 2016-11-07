from persistence import ServicoPersistence


def cadastra(servico):
    return ServicoPersistence.cadastra(servico)


def atualiza(request, servico, pk):
    return ServicoPersistence.atualiza(request, servico, pk)


def servico_por_id(pk):
    return ServicoPersistence.servico_por_id(pk)


def lista():
    return ServicoPersistence.lista()

