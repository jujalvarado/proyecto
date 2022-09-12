from django.shortcuts import render,redirect

from .models import Producto, Categoria_producto

# Create your views here.
def home (request):
    return render(request, "bienvenido.html")

def bienvenido (request):
    return render(request, "bienvenido.html")

def formulario_producto(request):
    return render(request,"formulario-producto.html")

def registrar_producto(request):
    nombre = request.POST['nombre']
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']
    proveedor = request.POST['proveedor']
    stock = request.POST['stock']
    precio_compra = request.POST['precio_compra']
    precio_venta = request.POST['precio_venta']

    producto = Producto.objects.create(nombre=nombre, categoria=categoria,descripcion=descripcion,proveedor=proveedor,
                                        stock=stock, precio_compra=precio_compra, precio_venta=precio_venta)
    return redirect('/')

    
def formulario_categoria_producto(request):
    return render(request,"formulario-categoria.html")

def registrar_categoria_producto(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    categoria= Categoria_producto.objects.create(codigo=codigo,nombre=nombre)
    
    return redirect('/')

