from django.contrib import admin
from .infrastructure.models import ServicioModel, ReservaModel

admin.site.register(ServicioModel)
admin.site.register(ReservaModel)