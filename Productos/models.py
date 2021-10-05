from django.db import models
#from Usuarios.models import *



class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.nombre

    

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(blank = True, null = True)
    calificacion = models.FloatField(default=0)
    marca = models.CharField(max_length=40, default ='')
    logo = models.ImageField(blank = True, null = True)
    ref = models.CharField(max_length=40, default ='')

    @property # convierte un metodo en tributo
    def tipoCategoria(self):
        from Productos.serializers import TipoSerial
        return TipoSerial(self.tipo).data 
    
    def __str__(self):
        return self.nombre
    @property
    def calcularCalificacion(self):
        comentarios = self.comentario_set.all()
        calificacion = 0
        for comentario in comentarios:
            calificacion += comentario.calificacion
        return calificacion/len(comentarios)

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.usuario + " - " + self.producto.nombre
        



