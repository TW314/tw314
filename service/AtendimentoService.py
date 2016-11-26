from persistence import AtendimentoPersistence


def cadastra(status, ticket, usuario):
    return AtendimentoPersistence.cadastra(status, ticket, usuario)
