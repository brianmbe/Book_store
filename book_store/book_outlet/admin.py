from django.contrib import admin

from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "ratings",)
    list_display = ("title", "author", "ratings",)


admin.site.register(Book, BookAdmin)
