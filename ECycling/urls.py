from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from ECycling.views import crea_clientes,ClienteListView,ClientesCreateView,ClienteDeleteView,ClienteUpdateView,index,muestra_nosotros


urlpatterns=[
    path('', index, name='index'),
   # path('admin/', admin.site.urls),
    path('crea_cliente/',ClientesCreateView.as_view(), name='crea_clientes'),
    path('lista_clientes/',ClienteListView.as_view()),
    path('borra_cliente/<int:pk>',ClienteDeleteView.as_view(), name='borra_cliente'),
    path('cliente_update/<int:pk>',ClienteUpdateView.as_view(),name='Actualiza'),
    path('productos/', include('productos.urls')),
    path('users/', include('users.urls')),
    path('users/profile/', include('users.urls')),
    path('nosotros/', muestra_nosotros)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
