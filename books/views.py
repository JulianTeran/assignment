from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Author, Book
from .forms import AuthorForm, BookForm

from datetime import datetime


# Create your views here.

book_list = Book.objects.all()
author_list = Author.objects.all()

books_with_authors = []
for book in book_list:
    book_with_author = book
    book_with_author.author = Author.objects.filter(pk=book.author_id).first()
    books_with_authors.append(book_with_author)

books_by_author = []
for author in author_list:
    author_books = Book.objects.filter(author_id=author.pk)
    if (author_books.count() > 0):
        books_by_author.append(
            (author, Book.objects.filter(author_id=author.pk)))


def index(request):
    return render(request, 'index.html', {"books_by_author": books_by_author})


def manage_books(request):
    return render(request, 'manage_books.html', {"author_list": author_list, "books_with_authors": books_with_authors})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print(request.POST)
        if form.is_valid():
            title_input = form.cleaned_data["title"]
            date_input = form.cleaned_data["date"]
            author_id_input = form.cleaned_data["author_id"]
            book = Book(title=title_input, pub_date=date_input,
                        author_id=author_id_input)
            book.save()
            return HttpResponseRedirect("/books/manage")
    return HttpResponse("FAILURE")


def delete_book(request):
    if request.method == "POST":
        book = Book.objects.all().filter(
            pk=int(request.POST["book_id"])).first()
        book.delete()
        return HttpResponseRedirect("/books/manage")
    return HttpResponse("FAILURE")


def manage_authors(request):
    return render(request, 'manage_authors.html', {"author_list": author_list})


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name_input = form.cleaned_data["first_name"]
            last_name_input = form.cleaned_data["last_name"]
            author = Author(first_name=first_name_input,
                            last_name=last_name_input)
            author.save()
            return HttpResponseRedirect("/books/authors/manage")
    return HttpResponse("FAILURE")


def delete_author(request):
    if request.method == "POST":
        author = Author.objects.all().filter(
            pk=int(request.POST["author_id"])).first()
        author.delete()
        return HttpResponseRedirect("/books/authors/manage")
    return HttpResponse("FAILURE")
