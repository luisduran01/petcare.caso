from rest_framework import serializers

class ServicioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)
    descripcion = serializers.CharField(required=False, allow_blank=True)
    precio = serializers.IntegerField(default=0)

class ReservaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dueño = serializers.DictField()
    mascota = serializers.DictField()
    
    # Hacemos que el frontend pueda enviar servicioNombre y que servicioId sea opcional
    servicioNombre = serializers.CharField(required=False, allow_blank=True)
    servicioId = serializers.IntegerField(required=False, default=1) 
    
    fecha = serializers.DateField()
    hora = serializers.TimeField()
    estado = serializers.CharField(default="confirmada", required=False)