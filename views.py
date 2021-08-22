from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    return redirect('/books')


# LIBROS!

def books(request):
    books = Books.objects.all()
    
    data = {
        'books': books,
    }
    return render(request, 'books.html', data)

def add_book(request):
    title = request.POST['title']
    desc =request.POST['desc']

    Books.objects.create(title=title, desc=desc)
    return redirect('/books')

def info_book(request, id):
    book = Books.objects.get(id=int(id))
    authors = Authors.objects.all()
    context = {
        'book':book,
        'authors': authors
    }
    
    return render(request, 'bookinfo.html', context)

def book_add_author(request):
    books = Books.objects.all()
    book_id = request.POST['id']
    idauthor = request.POST['idauthor']
    author = Authors.objects.get(id=idauthor)
    book = Books.objects.get(id=book_id)
    context = {
        'author': authors,
        'books': books,
        'book_id': book_id,
        'author': author,
    }
    author.books.add(book)
    camefrom = request.META.get('HTTP_REFERER')
    return redirect(camefrom)

# AUTORES!

def authors(request):
    authors = Authors.objects.all()
    books = Books.objects.all()
    
    data = {
        'authors': authors,
        'books': books,
    }
    return render(request, 'authors.html', data)

def add_author(request):
    first_name = request.POST['first_name']
    last_name =request.POST['last_name']
    notes = request.POST['notes']

    Authors.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def info_authors(request, id):
    author = Authors.objects.get(id=int(id))
    books = Books.objects.all()
    
    data = {
        'author': author,
        'books': books,
    }
    
    return render(request, 'authorinfo.html', data)

def author_add_book(request):
    authors = Authors.objects.all()
    author_id = request.POST['id']
    idbook = request.POST['bookid']
    book = Books.objects.get(id=idbook)
    author = Authors.objects.get(id=author_id)
    context = {
        'book': book,
        'authors': authors,
        'author_id': author_id,
        'author': author,
    }
    book.authors.add(author)
    camefrom = request.META.get('HTTP_REFERER')
    return redirect(camefrom)
