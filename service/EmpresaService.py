from persistence import EmpresaPersistence


def cadastra(empresa):
    return EmpresaPersistence.cadastra(empresa)


def atualiza(empresa, pk):
    return EmpresaPersistence.atualiza(empresa, pk)


def busca_por_cnpj(cnpj):
    return EmpresaPersistence.busca_por_cnpj(cnpj)


def lista():
    return EmpresaPersistence.lista()