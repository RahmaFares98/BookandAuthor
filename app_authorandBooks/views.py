from django.shortcuts import render,redirect,get_object_or_404
from . import models
from .models import Book ,Author
# Create your views here.
def index (request): #get data to fill what we need after
    Books= Book.objects.all() #gets all the records in the table
    context ={
            'Books':Books,}
    
    
    return render (request,'index.html',context)


def add_book(request):#Post ,Add data of Book 
    if request.method == 'POST':
        title = request.POST['title']
        description=request.POST['description']
        models.addBook(title=title,description=description)  #call addbook from Model
    return redirect('/')

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
        'authors': Author.objects.all()  # Accessing the related authors correctly
    }
    return render(request, 'book_details.html', context)


def add_author_to_book(request, book_id):# add author name for books
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = get_object_or_404(Author, id=author_id)
        book.authors.add(author)  # Add the author to the book's authors
        return redirect('book_detail', book_id=book_id)
    return redirect('book_detail', book_id=book_id)



def Authors (request):# to show Author Data templete
    Authors=Author.objects.all()#gets all the records in the table
    context ={
            'Authors': Authors}
    return render (request,'Author.html',context)


def add_Author(request):# add data for author 
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        Notes=request.POST['Notes']
        models.addAuthor(first_name=first_name,last_name=last_name,Notes=Notes)  
    return redirect('/Authors')

def Author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {
        'author': author,
        'all_books': Book.objects.all()
    }
    return render(request, 'Author_details.html', context)

def add_book_to_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        author.books.add(book)
        return redirect('author_detail', author_id=author_id)
    
    return redirect('author_detail', author_id=author_id)