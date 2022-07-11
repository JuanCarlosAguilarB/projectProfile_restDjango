from django.contrib import admin
from .models import UserProfile

# estamos dando acceso al administrador para que pueda editar el modelo de UserProfile. 
    # por ello fue que lo editamos 
admin.site.register(UserProfile)
