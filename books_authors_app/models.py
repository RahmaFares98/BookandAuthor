from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="old book")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name='books')
    



def add_book(title,desc):
    book=Book.objects.create(title=title,desc=desc)
    return book


def add_author(first_name,last_name,notes):
    Author=Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
    return Author

