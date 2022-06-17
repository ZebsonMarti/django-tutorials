from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .models import Author, Book


def create_book_view(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("book-detail", pk=book.id)
        else:
            return render(
                request, "bookshtmx/partials/book_form.html", context={"form": form}
            )

    context = {"form": form, "author": author, "books": books}

    return render(request, "bookshtmx/create_book.html", context)


def update_book_view(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("book-detail", pk=book.id)

    context = {"form": form, "book": book}

    return render(request, "bookshtmx/partials/book_form.html", context)


def delete_book_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def book_detail_view(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {"book": book}
    return render(request, "bookshtmx/partials/book_detail.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "bookshtmx/partials/book_form.html", context)
