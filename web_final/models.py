from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    age = models.IntegerField(default = 0, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return str(self.user.username)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    category = models.ForeignKey(Categoria)
    user = models.ForeignKey(User)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
       return str(self.nombre)

