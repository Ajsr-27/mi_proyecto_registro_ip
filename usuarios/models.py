from django.db import models

# Create your models here.
class RegistroUsuario(models.Model):
    nombre = models. CharField(max_length=100)
    email = models.EmailField(unique=True)
    ip = models.GenericIPAddressField()
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.nombre} 