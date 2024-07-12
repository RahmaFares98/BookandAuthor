from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        Book.objects.create(title=title)
    return redirect('book_list')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    authors = Author.objects.exclude(books=book)
    return render(request, 'book_detail.html', {'book': book, 'authors': authors})

def add_author_to_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        author_id = request.POST['author_id']
        author = get_object_or_404(Author, id=author_id)
        book.authors.add(author)
    return redirect('book_detail', book_id=book_id)

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        Author.objects.create(name=name)
    return redirect('author_list')

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.exclude(authors=author)
    return render(request, 'author_detail.html', {'author': author, 'books': books})

def add_book_to_author(request, author_id):
    if request.method == 'POST':
        author = get_object_or_404(Author, id=author_id)
        book_id = request.POST['book_id']
        book = get_object_or_404(Book, id=book_id)
        author.books.add(book)
    return redirect('author_detail', author_id=author_id)