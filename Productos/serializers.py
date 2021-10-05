from rest_framework import serializers
from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre','foto','tipo','descripcion','calcularCalificacion','marca','ref']

class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'