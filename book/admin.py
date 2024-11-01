from django.contrib import admin
from book.models import Book, Borrowing

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_per_page = 10 

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'client', 'borrowing_date', 'return_date', 'returned')
    list_filter = ('returned',)