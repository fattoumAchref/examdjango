from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.core.validators import MinLengthValidator

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        help_text="Le nom de la catégorie doit contenir entre 10 et 100 caractères."
    )
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.category_name






