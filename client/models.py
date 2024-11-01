from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Client(AbstractUser):
    library_identifier = models.CharField(
        max_length=255,
        unique=True,
        help_text=_("L'identifiant doit être unique et respecter le format: Majuscule au début, lettres, 4 chiffres."),
    )
    email = models.EmailField(
        unique=True,
        help_text=_("Veuillez entrer une adresse email valide appartenant au domaine gmail.com (ex: example@gmail.com).")
    )
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if not self.email.endswith("@gmail.com"):
            raise ValidationError(_("Veuillez entrer une adresse email appartenant au domaine gmail.com."))