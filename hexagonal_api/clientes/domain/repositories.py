from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Servicio, Reserva

class ServicioRepository(ABC):
    @abstractmethod
    def listar(self) -> List[Servicio]: ...

    @abstractmethod
    def obtener_por_id(self, servicio_id: int) -> Optional[Servicio]: ...

    @abstractmethod
    def guardar(self, servicio: Servicio) -> Servicio: ...

    @abstractmethod
    def eliminar(self, servicio_id: int) -> bool: ...


class ReservaRepository(ABC):
    @abstractmethod
    def listar(self) -> List[Reserva]: ...

    @abstractmethod
    def obtener_por_id(self, reserva_id: int) -> Optional[Reserva]: ...

    @abstractmethod
    def guardar(self, reserva: Reserva) -> Reserva: ...

    @abstractmethod
    def eliminar(self, reserva_id: int) -> bool: ...