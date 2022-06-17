from django.urls import path
from . import views

urlpatterns = [
    path("create-book/<pk>", views.create_book_view, name="create-book"),
]
