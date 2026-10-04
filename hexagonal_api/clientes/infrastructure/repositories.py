from ..domain.entities import Servicio, Reserva
from ..domain.repositories import ServicioRepository, ReservaRepository
from .models import ServicioModel, ReservaModel

# --- Mapeos para Servicio ---
def _to_entity_servicio(m: ServicioModel) -> Servicio:
    return Servicio(
        id=m.id,
        nombre=m.nombre,
        descripcion=m.descripcion,
        precio=m.precio
    )

class DjangoServicioRepository(ServicioRepository):
    def listar(self):
        return [_to_entity_servicio(m) for m in ServicioModel.objects.all()]

    def obtener_por_id(self, servicio_id: int):
        try:
            m = ServicioModel.objects.get(id=servicio_id)
            return _to_entity_servicio(m)
        except ServicioModel.DoesNotExist:
            return None

    def guardar(self, servicio: Servicio) -> Servicio:
        if servicio.id is None:
            m = ServicioModel.objects.create(
                nombre=servicio.nombre,
                descripcion=servicio.descripcion,
                precio=servicio.precio
            )
        else:
            m = ServicioModel.objects.get(id=servicio.id)
            m.nombre = servicio.nombre
            m.descripcion = servicio.descripcion
            m.precio = servicio.precio
            m.save()
        return _to_entity_servicio(m)

    def eliminar(self, servicio_id: int) -> bool:
        try:
            m = ServicioModel.objects.get(id=servicio_id)
            m.delete()
            return True
        except ServicioModel.DoesNotExist:
            return False


# --- Mapeos para Reserva ---
def _to_entity_reserva(m: ReservaModel) -> Reserva:
    return Reserva(
        id=m.id,
        dueno_nombre=m.dueno_nombre,
        dueno_telefono=m.dueno_telefono,
        mascota_nombre=m.mascota_nombre,
        mascota_tipo=m.mascota_tipo,
        mascota_raza=m.mascota_raza,
        servicio_id=m.servicio_id,
        fecha=m.fecha,
        hora=m.hora,
        estado=m.estado
    )

class DjangoReservaRepository(ReservaRepository):
    def listar(self):
        return [_to_entity_reserva(m) for m in ReservaModel.objects.all()]

    def obtener_por_id(self, reserva_id: int):
        try:
            m = ReservaModel.objects.get(id=reserva_id)
            return _to_entity_reserva(m)
        except ReservaModel.DoesNotExist:
            return None

    def guardar(self, reserva: Reserva) -> Reserva:
        # Buscamos la instancia del modelo Servicio para asignarla a la ForeignKey
        servicio_model = ServicioModel.objects.get(id=reserva.servicio_id)
        
        if reserva.id is None:
            m = ReservaModel.objects.create(
                dueno_nombre=reserva.dueno_nombre,
                dueno_telefono=reserva.dueno_telefono,
                mascota_nombre=reserva.mascota_nombre,
                mascota_tipo=reserva.mascota_tipo,
                mascota_raza=reserva.mascota_raza,
                servicio=servicio_model,
                fecha=reserva.fecha,
                hora=reserva.hora,
                estado=reserva.estado
            )
        else:
            m = ReservaModel.objects.get(id=reserva.id)
            m.dueno_nombre = reserva.dueno_nombre
            m.dueno_telefono = reserva.dueno_telefono
            m.mascota_nombre = reserva.mascota_nombre
            m.mascota_tipo = reserva.mascota_tipo
            m.mascota_raza = reserva.mascota_raza
            m.servicio = servicio_model
            m.fecha = reserva.fecha
            m.hora = reserva.hora
            m.estado = reserva.estado
            m.save()
        return _to_entity_reserva(m)

    def eliminar(self, reserva_id: int) -> bool:
        try:
            m = ReservaModel.objects.get(id=reserva_id)
            m.delete()
            return True
        except ReservaModel.DoesNotExist:
            return False