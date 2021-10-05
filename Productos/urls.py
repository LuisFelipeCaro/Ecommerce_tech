#Aca estamos espcificando las direcciones de las API

from rest_framework import urlpatterns
from Checkout.views import CarritoComprasAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Productos.views import ProductoAPI, TipoArticuloAPI, ComentarioAPI
from .views import *

router = DefaultRouter()
router.register('tipo', TipoArticuloAPI)
router.register('items',ProductoAPI)
router.register('comentario',ComentarioAPI, basename="comentario")
router.register('comentario',CarritoComprasAPI, basename="carrito")

urlpatterns = [
    path('dev/',include(router.urls))
]

#Direccion => localhost:8000/items/dev/