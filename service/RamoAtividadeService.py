from persistence import RamoAtividadePersistence


def cadastra(ramo_atividade):
    return RamoAtividadePersistence.cadastra(ramo_atividade)


def atualiza(request, ramo_atividade, pk):
    return RamoAtividadePersistence.atualiza(request, ramo_atividade, pk)


def ramo_por_id(pk):
    return RamoAtividadePersistence.ramo_por_id(pk)


def lista():
    return RamoAtividadePersistence.lista()

