from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import BaseUserManager 

class UserProfileManager(BaseUserManager):
    '''manager para perfiles de usuario'''
    def create_user(self,name, email, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        
        #normalize_email es para pasar el email a minuscula
        email = self.normalize_email(email)  
        #creando nuestro modelo
        user=self.model(email=email,name=name)
        #estableciendo el password del usuario
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    #definiendo funciones para los administradores     
    def create_superuser(self,name, email, password):
        
        #podemos llamar la función de crear usuario dado que super usuario tambien es un usuario
        user = self.create_user(name, email, password) 
        user.is_superuser = True   #  este atributo, is_superuser, se especifica automaticamente cuando 
            # heredamos de PermissionsMixin
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user 
    
        

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema """
    email = models.EmailField(max_length=254,unique=True)
    name =  models.CharField(unique=True,max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        '''obtener nombre complero del usuario'''
        return self.name   
    
    def get_short_name(self):
        '''obtener nombre corto usuario'''
        return self.name 
    
    def __str__(self):
        '''Retornar cadena representativa de nuestro usuario'''
        return self.email
    