from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.

admin.site.register(Author)
admin site.register(Language)

class BooksInline(admin.TabularInline):
	model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    list_filter = ('status', 'due_back')
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    
admin.site.unregister(Author)
admin.site.register(Author, AuthorAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id')
	list_filter = ['status', 'due_back']

	fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

 	