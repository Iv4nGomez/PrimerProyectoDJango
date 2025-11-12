from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('posts/<int:pk>', views.detalles_post, name='detalles_post'),
    path('autor/<int:pk>', views.autor_post, name='autor_post'),
    path('autores', views.autores, name="autores"),
    path('formulario', views.formulario, name="formulario"),
    path('autor/nuevo', views.autor_nuevo, name="autor_nuevo")

]
    