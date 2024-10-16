from django.contrib import admin
from .models import Author, Book, Authors, Bookshelves, Languages, Subjects, Bookshelf, Format, Language, Subject

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_year', 'death_year')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to search by
    ordering = ('name',)  # Default ordering

    # Optional: Define which fields to display in the detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'birth_year', 'death_year'),
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'gutenberg_id', 'download_count', 'media_type')
    search_fields = ('title',)
    list_filter = ('media_type',)
    ordering = ('-download_count',)


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('book', 'author_id')


@admin.register(Bookshelves)
class BookshelvesAdmin(admin.ModelAdmin):
    list_display = ('book', 'bookshelf')


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('book', 'language')


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('book', 'subject')


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('book', 'mime_type', 'url')
    list_filter = ('mime_type',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
