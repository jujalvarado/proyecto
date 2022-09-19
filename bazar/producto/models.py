from django.db import models

# Create your models here.


class Categoria_producto(models.Model):
    codigo= models.CharField(max_length=6)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)


class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    estado = models.SmallIntegerField(max_length=1, default=1)   

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.descripcion)


class Proveedor(models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion= models.TextField(max_length= 250)
    ruc = models.CharField(max_length=13)
    direccion = models.TextField(max_length= 250)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    estado = models.SmallIntegerField(max_length=1, default=1)   

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.descripcion)


class Proveedor_marca(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    estado = models.SmallIntegerField(max_length=1, default=1)  

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.proveedor, self.marca)
    
         
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria_producto,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length= 250)
    proveedor = models.ForeignKey(Proveedor_marca, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    precio_compra = models.DecimalField(max_digits=4,decimal_places=2)
    precio_venta = models.DecimalField(max_digits=4,decimal_places=2)
    estado = models.SmallIntegerField(max_length=1, default=1)   
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.stock)


class Producto_imagen(models.Model):
    producto = models.ForeignKey(Producto, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="uploads/",null=False,blank=True)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(Producto.nombre, Producto.descripcion)
