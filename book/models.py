from django.db import models
from client.models import Client
from category.models import Category
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="borrowings")
    borrowing_date = models.DateField()
    return_date = models.DateField()
    returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.client} borrowed {self.book}"

    def clean(self):
        if self.return_date < self.borrowing_date:
            raise ValidationError(_("La date de retour doit être postérieure ou égale à la date d'emprunt."))








