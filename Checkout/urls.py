from rest_framework import urlpatterns
from Checkout.views import CarritoComprasAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('carrito', CarritoComprasAPI, basename='carrito')
router.register('articulos', ArticuloAPI, basename='articulos')
router.register('carrito', InfoAPI, basename='informacion_envios')

urlpatterns = [
    path('dev/', include(router.urls))
]

#localhost:8000/Checkout/api/dev