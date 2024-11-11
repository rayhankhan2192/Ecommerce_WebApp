from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.utils import timezone

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(primary_key=True, unique=True, null=False, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
    
    def __srr__(self):
        return self.email
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
    
    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission."""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Check if the user has permissions for a specific app."""
        return self.is_superuser
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    home = models.TextField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"Address for {self.user.email}"   
    
