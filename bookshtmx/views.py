from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookFormSet


def create_book_view(request, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)
    ctx = {"formset": formset, "author": author}
    return render(request, "bookshtmx/create_book.html", ctx)
