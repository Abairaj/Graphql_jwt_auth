from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid

from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    email = models.EmailField(_('email address'), unique=True)
    user_id = models.UUIDField(default=uuid.uuid4())
    phone = models.CharField(
        max_length=150, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=150, choices=GENDER_CHOICES, null=True, blank=True)
    profile = models.ImageField(upload_to='profile')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = CustomUserManager()
