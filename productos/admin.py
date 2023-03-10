from django.contrib import admin
from productos.models import indumentaria
from productos.models import bicicletas


#admin.site.register(indumentaria)
@admin.register(indumentaria)
class IndumentariaAdmin(admin.ModelAdmin):
    list_display=('cod_indumentaria','tipo','nombre','stock','precio','imagen')


#admin.site.register(bicicletas)
@admin.register(bicicletas)
class BicicletaAdmin(admin.ModelAdmin):
    list_display=('tipo','nombre','rodado','precio','descuento','imagen')