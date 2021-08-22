from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors


def index(request):
    return redirect('/books')


# LIBROS!


# MUESTRA HTML CON TODOS LOS LIBROS DISPONIBLES
def books(request):
    books = Books.objects.all()

    data = {
        'books': books,
    }
    return render(request, 'books.html', data)

# FUNCION QUE ADICIONA UN NUEVO LIBRO - SOLICITA UN TITULO Y UNA DESCRIPCION
def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']

    Books.objects.create(title=title, desc=desc)
    return redirect('/books')

# MUESTRA HTML CON INFORMACION DEL LIBRO SELECCIONADO
def info_book(request, id):
    book = Books.objects.get(id=int(id))
    authors = Authors.objects.all()
    context = {
        'book': book,
        'authors': authors
    }

    return render(request, 'bookinfo.html', context)

# FUNCION QUE PERMITE ASOCIAR UN NUEVO AUTOR (DESDE BBDD) AL LIBRO SELECCIONADO
def book_add_author(request):
    authors = Authors.objects.all()
    print(authors)
    author_id = request.POST['id']
    print(author_id)
    idbook = request.POST['bookid']
    print(idbook)
    book = Books.objects.get(id=idbook)
    print(book)
    author = Authors.objects.get(id=author_id)
    print(author)
    context = {
        'book': book,
        'authors': authors,
        'author_id': author_id,
        'author': author
    }
    author.books.add(book)
    camefrom = request.META.get('HTTP_REFERER')
    return redirect(camefrom)

# AUTORES!


# MUESTRA HTML CON TODOS LOS AUTORES DISPONIBLES
def authors(request):
    authors = Authors.objects.all()
    books = Books.objects.all()
    
    data = {
        'authors': authors,
        'books': books,
    }
    return render(request, 'authors.html', data)

# FUNCION QUE ADICIONA UN NUEVO AUTOR - SOLICITA UN NOMBRE, APELLIDO Y UNA NOTA
def add_author(request):
    first_name = request.POST['first_name']
    last_name =request.POST['last_name']
    notes = request.POST['notes']

    Authors.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

# MUESTRA HTML CON INFORMACION DEL AUTOR SELECCIONADO
def info_authors(request, id):
    author = Authors.objects.get(id=int(id))
    books = Books.objects.all()
    
    data = {
        'author': author,
        'books': books,
    }
    
    return render(request, 'authorinfo.html', data)

# FUNCION QUE PERMITE ASOCIAR UN NUEVO LIBRO (DESDE BBDD) AL AUTOR SELECCIONADO
def author_add_book(request):
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
    book.authors.add(author)
    camefrom = request.META.get('HTTP_REFERER')
    return redirect(camefrom)
