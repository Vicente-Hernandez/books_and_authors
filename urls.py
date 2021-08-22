from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('add_book', views.add_book),
    path('books/<id>', views.info_book),
    path('book_add_author', views.book_add_author),
    
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<id>', views.info_authors),
    path('author_add_book', views.author_add_book),
]
