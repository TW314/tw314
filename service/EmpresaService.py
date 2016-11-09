from persistence import EmpresaPersistence


def cadastra(empresa):
    return EmpresaPersistence.cadastra(empresa)


def atualiza(empresa_novo, empresa, pk):
    return EmpresaPersistence.atualiza(empresa_novo, empresa, pk)


def busca_por_cnpj(cnpj):
    return EmpresaPersistence.busca_por_cnpj(cnpj)


def busca_por_id(id):
    return EmpresaPersistence.empresa_por_id(id)


def lista():
    return EmpresaPersistence.lista()