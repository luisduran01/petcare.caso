from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Servicio:
    nombre: str
    descripcion: str
    precio: int
    id: Optional[int] = None

@dataclass
class Reserva:
    dueno_nombre: str
    dueno_telefono: str
    mascota_nombre: str
    mascota_tipo: str
    mascota_raza: str
    servicio_id: int
    fecha: datetime.date
    hora: datetime.time
    estado: str = "confirmada"
    id: Optional[int] = None