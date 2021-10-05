from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND # => pagina no encontrada 
from Productos.models import *
from Productos.serializers import *


class TipoArticuloAPI (viewsets.ModelViewSet):
    serializer_class = TipoSerial
    queryset = Categoria.objects.all()


class ProductoAPI (viewsets.ModelViewSet):
    serializer_class = ProductoSerial
    queryset = Producto.objects.all()


class ComentarioAPI(viewsets.ViewSet):
    def list(self, request): # => GET
        comentarios = Comentario.objects.all()
        serializador = ComentarioSerial(comentarios, many=True)
        return Response(serializador.data)

    def create(self, request): # => Metodo POST
        serializador = ComentarioSerial(data=request.data)

        if serializador.is_valid(): # => Se verifica si el comentario cumple con requisitos de DB
            serializador.save()
            return Response ({"ComentarioExitoso": True})
        return Response (serializador.errors, HTTP_404_NOT_FOUND)
