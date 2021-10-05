from functools import partial
from Checkout.models import CarritoCompras
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import *

#-----------------------------------CARRITO-----------------------------------------#

class CarritoComprasAPI(viewsets.ViewSet):
    def list(self, request):
        carritos = CarritoCompras.objects.all()
        serializador = CarritoSerial(carritos, many=True)
        return Response(serializador.data)

    def create(self, request):
        serialCarrito = CarritoSerial(data=request.data)
        if serialCarrito.is_valid():
            serialCarrito.save()
            return Response({'Exito':True})
        return Response(serialCarrito.errors)

    def retrieve(self, request, pk=None):
        carritoUsuario = CarritoCompras.objects.filter(usuario=pk)
        carritoS = CarritoSerial(carritoUsuario, many=True)
        return (pk)


#-----------------------------------ARTICULO-----------------------------------------#

class ArticuloAPI(viewsets.ViewSet):
    def list(self, request):
        articulos = Articulo.objects.all()
        serializador = ArticuloSerial(articulos, many=True)
        return Response(serializador.data)

    def create(self, request):
        serializadorArticulo = ArticuloSerial(data=request.data)
        if serializadorArticulo.is_valid():
            serializadorArticulo.save()
            return Response({'Exito':True})
        return Response(serializadorArticulo.errors)

    def retrieve(self, request, pk=None):
        articuloUsuario = Articulo.objects.get(pk=pk)
        articuloSerializador = ArticuloSerial(articuloUsuario)
        return Response(articuloSerializador.data)


    def partial_update(self, request, pk=None):
        artModificar = Articulo.objects.get(pk=pk)
        articuloSerializador = ArticuloSerial(artModificar, request.data, partial=True)
        if articuloSerializador.is_valid():
            articuloSerializador.save()
            return Response({'Actualizado':True})
        return Response(articuloSerializador.errors)



#-----------------------------------INFO ENVIO-----------------------------------------#

class InfoAPI(viewsets.ViewSet):
    def list(self, request):
        envios = InfoEnvio.objects.all()
        serializador = InfoSerial(envios, many=True)
        return Response(serializador.data)

    def create(self, request):
        serialEnvio = InfoSerial(data=request.data)
        if serialEnvio.is_valid():
            serialEnvio.save()
            return Response({'Exito':True})
        return Response(serialEnvio.errors)

    def retrieve(self, request,pk=None):
        envioUsurio = Articulo.objects.filter(usuario=pk)
        envioS = InfoSerial(envioUsurio, many=True)
        return Response (pk)



