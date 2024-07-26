from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import FileExtensionValidator

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class User(AbstractUser):
    image = models.ImageField(
        upload_to='profile/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    is_employer = models.BooleanField(
        choices=BOOL_CHOICES,
        null=True,
        blank=True,
        default=False
    )
    resume = models.FileField(
        upload_to='resume/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'pdf'])]
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Ensure this name is unique within your project
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Ensure this name is unique within your project
        blank=True
    )

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
