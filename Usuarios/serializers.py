from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from Usuarios.models import *

class UsuarioSerial(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email','password']
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {
                    'input_type' : 'password'
                }
            }
        }

class PerfilSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ['usuario','nombres','apellidos','pais','departamento','ciudad']