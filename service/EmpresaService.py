from persistence import EmpresaPersistence


def busca_por_cnpj(cnpj):
    return EmpresaPersistence.busca_por_cnpj(cnpj)

def lista():
    return EmpresaPersistence.lista()
