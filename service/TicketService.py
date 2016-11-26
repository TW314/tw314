from persistence import TicketPersistence


def mostrar_fila(empresa, servico):
    return TicketPersistence.mostrar_fila(empresa, servico)


def mostrar_ticket(empresa, servico):
    return TicketPersistence.mostrar_ticket(empresa, servico)


def chamar_ticket(empresa, servico):
    return TicketPersistence.chamar_ticket(empresa, servico)


def mudar_status_ticket(pk, status):
    return TicketPersistence.mudar_status_ticket(pk, status)
