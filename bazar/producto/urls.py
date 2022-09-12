from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('bienvenido',views.bienvenido, name='bienvenido'),
    path('formulario_producto',views.formulario_producto, name='formulario_producto'),
    path('registrar_producto',views.registrar_producto, name='registrar_producto'),
    
    path('formulario_categoria_producto',views.formulario_categoria_producto, name='formulario_categoria_producto'),
    path('registrar_categoria_producto',views.registrar_categoria_producto, name='registrar_categoria_producto'),

]