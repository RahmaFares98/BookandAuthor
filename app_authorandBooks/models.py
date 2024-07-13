from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="old book")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    Notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book, related_name='authors')
    updated_at = models.DateTimeField(auto_now=True)

def addBook(title,description):
    book=Book.objects.create(title=title,description=description)
    return book


def addAuthor(first_name,last_name,Notes):
    Author_data=Author.objects.create(first_name=first_name,last_name=last_name ,Notes=Notes)
    return Author_data


