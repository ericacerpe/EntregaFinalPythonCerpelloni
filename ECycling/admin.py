from django.contrib import admin
from ECycling.models import cliente
#admin.site.register(cliente)

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','direccion')
    



