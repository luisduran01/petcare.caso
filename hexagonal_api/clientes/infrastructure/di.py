from .repositories import DjangoServicioRepository, DjangoReservaRepository

def get_servicio_repository():
    return DjangoServicioRepository()

def get_reserva_repository():
    return DjangoReservaRepository()