from persistence import ServicoPersistence


def cadastra(servico):
    return ServicoPersistence.cadastra(servico)


def atualiza(servico, pk):
    return ServicoPersistence.atualiza(servico, pk)


def lista():
    return ServicoPersistence.lista()

