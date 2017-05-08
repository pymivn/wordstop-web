from django.shortcuts import render

from .models import Book, Word


def index(request):
    top_books = Book.objects.all()[:15]
    context = {'top_books': top_books}
    return render(request, 'words/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    words = Word.objects.filter(book_id=book_id).order_by('-frequency')
    context = {'book': book, 'words': words}

    return render(request, 'words/book_detail.html', context)
