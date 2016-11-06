from persistence import EmpresaPersistence


def busca_por_cnpj(empresa):
    return EmpresaPersistence.busca_por_cnpj(empresa)

def lista():
    return EmpresaPersistence.lista()
