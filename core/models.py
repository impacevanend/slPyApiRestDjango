from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Crear y guardar un nuevo usuario """
        user = self.model(email=email, **extra_fields)
        #* Contraseña no visible al usuario
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Modelo personalizado de usuaior que soporta hacer login con email en vez de usuario"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    #No queremos que la gene común sea administrador
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    #Queremos hacer login con email
    USERNAME_FIELD = 'email'