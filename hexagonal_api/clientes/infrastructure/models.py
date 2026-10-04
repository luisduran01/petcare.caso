from django.db import models

class ServicioModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(default=0)

    class Meta:
        db_table = "petcare_servicio"

    def __str__(self):
        return self.nombre


class ReservaModel(models.Model):
    # Subdocumento 'dueño' aplanado a columnas
    dueno_nombre = models.CharField(max_length=100)
    dueno_telefono = models.CharField(max_length=20)
    
    # Subdocumento 'mascota' aplanado a columnas
    mascota_nombre = models.CharField(max_length=100)
    mascota_tipo = models.CharField(max_length=50)
    mascota_raza = models.CharField(max_length=50)
    
    # Relación equivalente al servicioId (relacional)
    servicio = models.ForeignKey(ServicioModel, on_delete=models.CASCADE)
    
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50, default="confirmada")

    class Meta:
        db_table = "petcare_reserva"

    def __str__(self):
        return f"Reserva {self.id} - {self.mascota_nombre}"