from rest_framework import serializers
from .models import Book, Author, Format, Subject, Bookshelf, Language

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_year', 'death_year']

class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['mime_type', 'url']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    download_links = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'gutenberg_id', 
            'title', 
            'author', 
            'media_type', 
            'download_count', 
            'languages', 
            'subjects', 
            'bookshelves', 
            'download_links'
        ]

    # Custom method to retrieve the authors via the `Authors` model
    def get_author(self, obj):
        authors = obj.authors_set.all()  # Accessing related `Authors` entries
        return AuthorSerializer([author.author for author in authors], many=True).data

    # Custom method to retrieve download links via the `Format` model
    def get_download_links(self, obj):
        formats = obj.format_set.all()  # Accessing related `Format` entries
        return FormatSerializer(formats, many=True).data

    # Custom method to retrieve subjects via the `Subjects` model
    def get_subjects(self, obj):
        subjects = obj.subjects_set.all()  # Accessing related `Subjects` entries
        return SubjectSerializer([subject.subject for subject in subjects], many=True).data

    # Custom method to retrieve bookshelves via the `Bookshelves` model
    def get_bookshelves(self, obj):
        bookshelves = obj.bookshelves_set.all()  # Accessing related `Bookshelves` entries
        return BookshelfSerializer([bookshelf.bookshelf for bookshelf in bookshelves], many=True).data

    # Custom method to retrieve languages via the `Languages` model
    def get_languages(self, obj):
        languages = obj.languages_set.all()  # Accessing related `Languages` entries
        return LanguageSerializer([language.language for language in languages], many=True).data
