from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from ECycling.views import crea_clientes,lista_clientes,ClienteListView,actualiza_clientes,ClientesCreateView,ClienteDeleteView,ClienteUpdateView,index


urlpatterns=[
    path('', index, name='index'),
   # path('admin/', admin.site.urls),
    path('crea_cliente/',ClientesCreateView.as_view(), name='crea_clientes'),
    path('lista_clientes/',ClienteListView.as_view()),
    path('borra_cliente/<int:pk>',ClienteDeleteView.as_view(), name='borra_cliente'),
    path('cliente_update/<int:pk>',ClienteUpdateView.as_view(),name='Actualiza'),
    #path('cliente_update/<int:pk>',actualiza_clientes),
    #path('crea_indumentaria/',crea_indumentaria),
    #path('lista_indumentaria/',lista_indumentaria),
    #path('crea_bicicletas/',crea_bicicletas),
    #path('lista_bicicleta/',lista_bicicleta),
    path('productos/', include('productos.urls')),
    path('users/', include('users.urls')),
   
 

]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)