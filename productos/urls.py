from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from productos.views import crea_indumentaria,lista_indumentaria,crea_bicicletas,lista_bicicleta,IndumentariaUpdateView,IndumentariaDeleteView,BicicletaUpdateView,BicicletaDeleteView
from ECycling.views import index 

urlpatterns=[
    path('', index, name='index'),
   
    path('crea_indumentaria/',crea_indumentaria),
    path('lista_indumentaria/',lista_indumentaria),
    path('actualiza_indumentaria/<int:pk>',IndumentariaUpdateView.as_view(),name='Actualiza'),
    path('borra_indumentaria/<int:pk>',IndumentariaDeleteView.as_view(),name='Elimina'),

    path('crea_bicicletas/',crea_bicicletas),
    path('lista_bicicleta/',lista_bicicleta),
    path('actualiza_bicicletas/<int:pk>',BicicletaUpdateView.as_view(),name='Actualiza'),
    path('borra_bicicletas/<int:pk>',BicicletaDeleteView.as_view(),name='Elimina'),
 

]