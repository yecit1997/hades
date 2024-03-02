
from django.db import models
from datetime import datetime



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def _str_(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']




class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='producto', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def _str_(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']




class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField(default=datetime.now)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(max_length=15, default='none')
    
    def _str_(self) -> str:
        return f'{self.nombre} {self.apellidos}'
    
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']
    
    

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    
    def _str_(self) -> str:
        return self.cliente.nombre
    
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']





class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    
    def _str_(self) -> str:
        return self.producto.nombre
    
    class Meta:
        verbose_name = 'Detalle_venta'
        verbose_name_plural = 'Detalle_ventas'
        db_table = 'detalle_venta'
        ordering = ['id']

