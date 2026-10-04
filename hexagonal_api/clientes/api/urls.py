from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Servicio
    path("servicios/", views.ServicioListCreateView.as_view(), name="servicio-list-create"),
    path("servicios/<int:servicio_id>/", views.ServicioDetailView.as_view(), name="servicio-detail"),

    # Rutas para Reserva
    path("reservas/", views.ReservaListCreateView.as_view(), name="reserva-list-create"),
    path("reservas/<int:reserva_id>/", views.ReservaDetailView.as_view(), name="reserva-detail"),
]