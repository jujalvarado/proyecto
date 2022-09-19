from django.shortcuts import render,redirect

from .models import Producto, Categoria_producto, Proveedor_marca,Producto_imagen

# Create your views here.
def home (request):
    return render(request, "bienvenido.html")

def bienvenido (request):
    return render(request, "bienvenido.html")

def formulario_producto(request):
    listar_producto = Producto.objects.all()
    listar_imagen=Producto_imagen.objects.all()
    listar_categoria = Categoria_producto.objects.all()
    listar_proveedor = Proveedor_marca.objects.all()
    return render(request,"formulario-producto.html",
                {"categorias": listar_categoria,"proveedores": listar_proveedor,
                'productos':listar_producto, "imagenes":listar_imagen})

def registrar_producto(request):
    nombre = request.POST['nombre']
    categoria_id = request.POST['categoria']
    categoria = Categoria_producto.objects.get(id=categoria_id)
    descripcion = request.POST['descripcion']
    proveedor_id = request.POST['proveedor']
    proveedor = Proveedor_marca.objects.get(id=proveedor_id)
    stock = request.POST['stock']
    precio_compra = request.POST['precio_compra']
    precio_venta = request.POST['precio_venta']

    producto = Producto.objects.create(nombre=nombre, categoria=categoria,descripcion=descripcion,proveedor=proveedor,
                                        stock=stock, precio_compra=precio_compra, precio_venta=precio_venta)
    
    imagenes = request.FILES.getlist('imagen')
    producto_id= producto.pk
    producto = Producto.objects.get(pk=producto_id)
    for imagen in imagenes:
        producto_imagen = Producto_imagen.objects.create(
            producto=producto,
            imagen=imagen
        )

    return redirect('/formulario_producto')

    
def formulario_categoria_producto(request):
    listar_categoria = Categoria_producto.objects.all()
    return render(request,"formulario-categoria.html",{
        "categorias": listar_categoria})

def registrar_categoria_producto(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    categoria= Categoria_producto.objects.create(codigo=codigo,nombre=nombre)
    
    return redirect('/formulario_categoria_producto')

