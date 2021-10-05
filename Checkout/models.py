from django.db import models
from Productos.models import Producto
from Usuarios.models import *
from django.contrib.auth import get_user_model

class CarritoCompras (models.Model):
    usuario = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descuento = models.FloatField(default=0)
    cantidad_minima = models.IntegerField(default=0)
    pago_realizado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario) + ' - ' + str(self.fecha)

    @property
    def total(self):
        total = 0
        articulos = Articulo.objects.filter(carrito=self)
        for articulo in articulos:
            total+=articulo.subtotal()
        return total

    def numero_articulos(self):
        articulos = Articulo.objects.filter(carrito=self)
        return len(articulos)

class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + ' / ' + self.producto.__str__()

    def subtotal(self):
        return self.producto.precio*self.cantidad

class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()

        

