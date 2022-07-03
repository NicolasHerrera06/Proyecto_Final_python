from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('' , views.inicio, name="Inicio"),
    path('login/' , views.login_request, name="Login"),
    path('register/' , views.register, name="Register"),
    path('logout/' , LogoutView.as_view(template_name='Blog/logout.html'), name='Logout'),
    path('contactos/' , views.contacto, name="Contacto"),
    path('crear-publicacion/' , views.agregar_post, name="Agregar_post"),
    path('listar-publicacion/' , views.listar_post, name="listar_post"),
    path('modificar-publicacion/<id>/' , views.modificar_post, name="modificar_post"),
    path('eliminar-publicacion/<id>/' , views.eliminar_post, name="eliminar_post"),
]