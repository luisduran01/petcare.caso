import dataclasses
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..infrastructure.di import get_servicio_repository, get_reserva_repository
from ..application.use_cases import (
    ListarServiciosUseCase, ObtenerServicioUseCase, CrearServicioUseCase, ActualizarServicioUseCase, EliminarServicioUseCase,
    ListarReservasUseCase, ObtenerReservaUseCase, CrearReservaUseCase, ActualizarReservaUseCase, EliminarReservaUseCase
)
from ..application.exceptions import EntidadNoEncontradaError
from .serializers import ServicioSerializer, ReservaSerializer

# ==========================================
# VISTAS PARA: SERVICIO (Plano, sin anidamiento)
# ==========================================
class ServicioListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        repo = get_servicio_repository()
        servicios = ListarServiciosUseCase(repo).ejecutar()
        data = [dataclasses.asdict(s) for s in servicios]
        return Response({"datos": data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ServicioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        repo = get_servicio_repository()
        servicio = CrearServicioUseCase(repo).ejecutar(serializer.validated_data)
        return Response(dataclasses.asdict(servicio), status=status.HTTP_201_CREATED)

class ServicioDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, servicio_id):
        repo = get_servicio_repository()
        try:
            servicio = ObtenerServicioUseCase(repo).ejecutar(servicio_id)
            return Response(dataclasses.asdict(servicio), status=status.HTTP_200_OK)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, servicio_id):
        serializer = ServicioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        repo = get_servicio_repository()
        try:
            servicio = ActualizarServicioUseCase(repo).ejecutar(servicio_id, serializer.validated_data)
            return Response(dataclasses.asdict(servicio), status=status.HTTP_200_OK)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, servicio_id):
        repo = get_servicio_repository()
        try:
            EliminarServicioUseCase(repo).ejecutar(servicio_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)


# ==========================================
# VISTAS PARA: RESERVA (Traducción NoSQL <-> SQL)
# ==========================================
def formatear_respuesta_nosql(reserva):
    return {
        "_id": reserva.id,
        "dueño": {
            "nombre": reserva.dueno_nombre,
            "telefono": reserva.dueno_telefono
        },
        "mascota": {
            "nombre": reserva.mascota_nombre,
            "tipo": reserva.mascota_tipo,
            "raza": reserva.mascota_raza
        },
        "servicioId": reserva.servicio_id,
        "servicioNombre": "Control Veterinario",
        "fecha": reserva.fecha,
        "hora": reserva.hora,
        "estado": reserva.estado
    }

class ReservaListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        repo = get_reserva_repository()
        reservas = ListarReservasUseCase(repo).ejecutar()
        data = [formatear_respuesta_nosql(r) for r in reservas]
        return Response({"datos": data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos_entrada = serializer.validated_data

        datos_planos = {
            "dueno_nombre": datos_entrada["dueño"]["nombre"],
            "dueno_telefono": datos_entrada["dueño"]["telefono"],
            "mascota_nombre": datos_entrada["mascota"]["nombre"],
            "mascota_tipo": datos_entrada["mascota"]["tipo"],
            "mascota_raza": datos_entrada["mascota"]["raza"],
            "servicio_id": datos_entrada.get("servicioId", 1), 
            "fecha": datos_entrada["fecha"],
            "hora": datos_entrada["hora"],
            "estado": datos_entrada.get("estado", "confirmada")
        }

        repo = get_reserva_repository()
        reserva = CrearReservaUseCase(repo).ejecutar(datos_planos)
        
        # Respuesta compuesta (Mensaje + Datos)
        return Response({
            "mensaje": "¡Reserva creada exitosamente en la base de datos SQL!",
            "datos": formatear_respuesta_nosql(reserva)
        }, status=status.HTTP_201_CREATED)

class ReservaDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, reserva_id):
        repo = get_reserva_repository()
        try:
            reserva = ObtenerReservaUseCase(repo).ejecutar(reserva_id)
            return Response(formatear_respuesta_nosql(reserva), status=status.HTTP_200_OK)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, reserva_id):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos_entrada = serializer.validated_data

        datos_planos = {
            "dueno_nombre": datos_entrada["dueño"]["nombre"],
            "dueno_telefono": datos_entrada["dueño"]["telefono"],
            "mascota_nombre": datos_entrada["mascota"]["nombre"],
            "mascota_tipo": datos_entrada["mascota"]["tipo"],
            "mascota_raza": datos_entrada["mascota"]["raza"],
            "servicio_id": datos_entrada.get("servicioId", 1),
            "fecha": datos_entrada["fecha"],
            "hora": datos_entrada["hora"],
            "estado": datos_entrada.get("estado", "confirmada")
        }

        repo = get_reserva_repository()
        try:
            reserva = ActualizarReservaUseCase(repo).ejecutar(reserva_id, datos_planos)
            
            # Respuesta compuesta (Mensaje + Datos)
            return Response({
                "mensaje": f"Reserva {reserva_id} actualizada correctamente.",
                "datos": formatear_respuesta_nosql(reserva)
            }, status=status.HTTP_200_OK)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, reserva_id):
        repo = get_reserva_repository()
        try:
            EliminarReservaUseCase(repo).ejecutar(reserva_id)
            
            # Cambiamos 204 No Content por 200 OK para que React pueda leer el JSON
            return Response({
                "mensaje": f"La reserva {reserva_id} fue eliminada de forma permanente."
            }, status=status.HTTP_200_OK)
        except EntidadNoEncontradaError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)