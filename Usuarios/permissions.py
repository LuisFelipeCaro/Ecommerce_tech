#Creacion de permisos de ussuario para la aplicacion
from rest_framework.permissions import BasePermission

class CreacionUsuario(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        elif request.user.is_authenticated and obj.username == request.user.username:
            return True
        return False

class AccesoInfoPersonal(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if hasattr(obj, 'username'):
            return True

        else:
            if request.user.username == obj.username:
                return True
        return False

    
