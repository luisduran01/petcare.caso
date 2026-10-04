from .exceptions import EntidadNoEncontradaError
from ..domain.entities import Servicio, Reserva
from ..domain.repositories import ServicioRepository, ReservaRepository

# ==========================================
# CASOS DE USO PARA: SERVICIO
# ==========================================

class ListarServiciosUseCase:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    def ejecutar(self):
        return self.repo.listar()

class ObtenerServicioUseCase:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    def ejecutar(self, servicio_id: int):
        servicio = self.repo.obtener_por_id(servicio_id)
        if not servicio:
            raise EntidadNoEncontradaError("Servicio no encontrado")
        return servicio

class CrearServicioUseCase:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    def ejecutar(self, datos: dict) -> Servicio:
        servicio = Servicio(
            nombre=datos["nombre"],
            descripcion=datos.get("descripcion", ""),
            precio=datos.get("precio", 0)
        )
        return self.repo.guardar(servicio)

class ActualizarServicioUseCase:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    def ejecutar(self, servicio_id: int, datos: dict) -> Servicio:
        servicio = self.repo.obtener_por_id(servicio_id)
        if not servicio:
            raise EntidadNoEncontradaError("Servicio no encontrado")
        
        servicio.nombre = datos.get("nombre", servicio.nombre)
        servicio.descripcion = datos.get("descripcion", servicio.descripcion)
        servicio.precio = datos.get("precio", servicio.precio)
        
        return self.repo.guardar(servicio)

class EliminarServicioUseCase:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo
    def ejecutar(self, servicio_id: int) -> bool:
        if not self.repo.eliminar(servicio_id):
            raise EntidadNoEncontradaError("Servicio no encontrado")
        return True

# ==========================================
# CASOS DE USO PARA: RESERVA
# ==========================================

class ListarReservasUseCase:
    def __init__(self, repo: ReservaRepository):
        self.repo = repo
    def ejecutar(self):
        return self.repo.listar()

class ObtenerReservaUseCase:
    def __init__(self, repo: ReservaRepository):
        self.repo = repo
    def ejecutar(self, reserva_id: int):
        reserva = self.repo.obtener_por_id(reserva_id)
        if not reserva:
            raise EntidadNoEncontradaError("Reserva no encontrada")
        return reserva

class CrearReservaUseCase:
    def __init__(self, repo: ReservaRepository):
        self.repo = repo
    def ejecutar(self, datos: dict) -> Reserva:
        reserva = Reserva(
            dueno_nombre=datos["dueno_nombre"],
            dueno_telefono=datos["dueno_telefono"],
            mascota_nombre=datos["mascota_nombre"],
            mascota_tipo=datos["mascota_tipo"],
            mascota_raza=datos["mascota_raza"],
            servicio_id=datos["servicio_id"],
            fecha=datos["fecha"],
            hora=datos["hora"],
            estado=datos.get("estado", "confirmada")
        )
        return self.repo.guardar(reserva)

class ActualizarReservaUseCase:
    def __init__(self, repo: ReservaRepository):
        self.repo = repo
    def ejecutar(self, reserva_id: int, datos: dict) -> Reserva:
        reserva = self.repo.obtener_por_id(reserva_id)
        if not reserva:
            raise EntidadNoEncontradaError("Reserva no encontrada")
        
        reserva.dueno_nombre = datos.get("dueno_nombre", reserva.dueno_nombre)
        reserva.dueno_telefono = datos.get("dueno_telefono", reserva.dueno_telefono)
        reserva.mascota_nombre = datos.get("mascota_nombre", reserva.mascota_nombre)
        reserva.mascota_tipo = datos.get("mascota_tipo", reserva.mascota_tipo)
        reserva.mascota_raza = datos.get("mascota_raza", reserva.mascota_raza)
        reserva.servicio_id = datos.get("servicio_id", reserva.servicio_id)
        reserva.fecha = datos.get("fecha", reserva.fecha)
        reserva.hora = datos.get("hora", reserva.hora)
        reserva.estado = datos.get("estado", reserva.estado)
        
        return self.repo.guardar(reserva)

class EliminarReservaUseCase:
    def __init__(self, repo: ReservaRepository):
        self.repo = repo
    def ejecutar(self, reserva_id: int) -> bool:
        if not self.repo.eliminar(reserva_id):
            raise EntidadNoEncontradaError("Reserva no encontrada")
        return True