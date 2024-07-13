from . import views
from django.urls import path


urlpatterns=[
    path ('', views.index , name='index'),
    path('add_book',views.add_book),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/<int:author_id>/add_book/', views.add_book_to_author, name='add_book_to_author'),
    path('authors',views.Authors ,name='authors'),
    path('add_Author',views.add_Author),
    path('authors/<int:author_id>/', views.Author_detail, name='author_detail'),
    path('book/<int:book_id>/add_author/', views.add_author_to_book, name='add_author_to_book'),  # URL for adding author to book


]