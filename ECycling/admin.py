from django.contrib import admin
from ECycling.models import cliente
from ECycling.models import personalizacion
#admin.site.register(cliente)

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','direccion')


@admin.register(personalizacion)
class PoratadaAdmin(admin.ModelAdmin):
    list_display=('titulo','imagen_portada')
    



