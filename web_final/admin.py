from django.contrib import admin

# Register your models here.
from web_final.models import UserProfile, Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)