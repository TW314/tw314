from persistence import EmpresaServicoPersistence


def cadastra(rel_emp_svc):
    return EmpresaServicoPersistence.cadastra(rel_emp_svc)


def atualiza(request, rel, pk):
    return EmpresaServicoPersistence.atualiza(request, rel, pk)


def lista(empresa):
    return EmpresaServicoPersistence.lista(empresa)
