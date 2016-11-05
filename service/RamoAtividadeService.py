from persistence import RamoAtividadePersistence


def cadastra(ramo_atividade):
    return RamoAtividadePersistence.cadastra(ramo_atividade)


def atualiza(ramo_atividade, pk):
    return RamoAtividadePersistence.atualiza(ramo_atividade, pk)


def lista():
    return RamoAtividadePersistence.lista()

