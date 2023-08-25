from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/manage", views.manage_authors, name="manage_authors"),
    path("manage", views.manage_books, name="manage_books"),
    path("delete", views.delete_book, name="delete_book"),
    path("create", views.create_book, name="create_book"),
    path("authors/create", views.create_author, name="create_author"),
    path("authors/delete", views.delete_author, name="delete_author")
]
