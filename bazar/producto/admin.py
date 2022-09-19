from django.contrib import admin

# Register your models here.

from .models import Categoria_producto,Proveedor, Marca,Proveedor_marca,Producto,Producto_imagen
admin.site.register(Categoria_producto)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Proveedor_marca)
admin.site.register(Producto_imagen)
admin.site.register(Producto)


