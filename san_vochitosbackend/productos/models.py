from django.db import models

# Create your models here.

class Project (models.Model):
    nombre = models.CharField(max_length=100, verbose_name = "Título")
    descripcion = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to="productos")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificación")
    
    def __str__(self):
        return self.nombre
    
    
   
   
   
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-created"]