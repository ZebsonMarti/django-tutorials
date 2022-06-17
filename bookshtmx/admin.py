from django.contrib import admin

# Register your models here.
from .models import Author, Book


class BookInlineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]


admin.site.register(Author, AuthorAdmin)
