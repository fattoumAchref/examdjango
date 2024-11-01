from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book, Borrowing
# Create your views here.


def book_list(request):
    books = Book.objects.all().order_by('-publication_date')  # Tri par date de publication
    return render(request, 'book_list.html', {'books': books})

def book_borrowings(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    borrowings = Borrowing.objects.filter(book=book)

    if not borrowings:
        message = "aucun emprunt"
    else:
        message = None
    
    return render(request, 'book_borrowings.html', {'book': book, 'borrowings': borrowings, 'message': message})
