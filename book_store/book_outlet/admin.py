from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "ratings",)
    list_display = ("title", "author", "ratings",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


class CountryAdmin(admin.ModelAdmin):
    list_filter = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Address)
