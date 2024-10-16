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
    class Meta:
        verbose_name_plural = "authors"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'gutenberg_id', 'download_count', 'media_type')
    search_fields = ('title',)
    list_filter = ('media_type',)
    ordering = ('-download_count',)

    class Meta:
        verbose_name_plural = "books"

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('book', 'author_id')

    class Meta:
        verbose_name_plural = "authormappings"

@admin.register(Bookshelves)
class BookshelvesAdmin(admin.ModelAdmin):
    list_display = ('book', 'bookshelf')

    class Meta:
        verbose_name_plural = "bookshelfmappings"

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('book', 'language')

    class Meta:
        verbose_name_plural = "languagemappings"

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('book', 'subject')

    class Meta:
        verbose_name_plural = "subjectmappings"

@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Meta:
        verbose_name_plural = "bookshelves"

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('book', 'mime_type', 'url')
    list_filter = ('mime_type',)

    class Meta:
        verbose_name_plural = "formats"

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code',)

    class Meta:
        verbose_name_plural = "languages"

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    class Meta:
        verbose_name_plural = "subjects"
