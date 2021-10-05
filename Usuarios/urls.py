from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Usuarios.views import *

router = DefaultRouter()
router.register('usuarios', UsuariosAPI)
router.register('perfiles', PerfilAPI)


urlpatterns = [
    path('dev/', include(router.urls)),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),

]
