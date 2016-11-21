from persistence import EmpresaServicoPersistence


def cadastra(rel_emp_svc):
    return EmpresaServicoPersistence.cadastra(rel_emp_svc)


def atualiza(request, rel, pk):
    return EmpresaServicoPersistence.atualiza(request, rel, pk)


def busca_por_cnpj(cnpj):
    return EmpresaServicoPersistence.busca_por_cnpj(cnpj)


def busca_por_id(id):
    return EmpresaServicoPersistence.empresa_por_id(id)


def lista():
    return EmpresaServicoPersistence.lista()