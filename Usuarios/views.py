#Serializadores de usuarios y perfiles
from rest_framework import viewsets, views
from rest_framework import authentication, permissions
from rest_framework.response import Response
from Usuarios.serializers import *
from django.contrib.auth import get_user_model, login, logout
from Usuarios.permissions import AccesoInfoPersonal
from django.shortcuts import get_object_or_404





class UsuariosAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoInfoPersonal)
    serializer_class = UsuarioSerial
    queryset = get_user_model().objects.all()

class PerfilAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AccesoInfoPersonal)
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()

class Logout(views.APIView):
    def get(self, request):
        if not request.user.anonymous:
            logout(request)
            return Response('El usuario ha hecho logout')
        return Response('Es un usuario anonimo')

class Login(views.APIView):
    def post(self, request):
        if 'username' in request.data and 'password' in request.data:
            usuario = get_object_or_404(get_user_model(),username = request.data['username'])
            if usuario.check_password(request.data['password']):
                login(request, usuario)
                return Response('El usuario ' + usuario.username + 'ha hecho login')
            return Response({'Login':False})
        return Response('Informacion erronea o incompleta')


            

