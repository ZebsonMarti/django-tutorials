from django.urls import path
from . import views

urlpatterns = [
    path("create-book/<pk>/", views.create_book_view, name="create-book"),
    path("book-form/", views.create_book_form, name="create-book-form"),
    path("book-detail/<pk>/", views.book_detail_view, name="book-detail"),
    path("book/<pk>/update/", views.update_book_view, name="update-book"),
    path("book/<pk>/delete/", views.delete_book_view, name="delete-book"),
]
