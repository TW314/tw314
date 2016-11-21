from persistence import EmpresaPersistence


def cadastra(empresa):
    return EmpresaPersistence.cadastra(empresa)


def atualiza(request, empresa, pk):
    return EmpresaPersistence.atualiza(request, empresa, pk)


def busca_por_cnpj(cnpj):
    return EmpresaPersistence.busca_por_cnpj(cnpj)


def busca_por_id(id):
    return EmpresaPersistence.empresa_por_id(id)


def lista():
    return EmpresaPersistence.lista()
