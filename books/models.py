# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    birth_year = models.IntegerField()
    death_year = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'books_author'
        verbose_name_plural = "authors"


class Book(models.Model):
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_book'
        verbose_name_plural = "books"


class Authors(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, related_name='authors_set')
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)
        verbose_name_plural = "author_mappings"


class Bookshelves(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, related_name='bookshelves_set')
    bookshelf = models.ForeignKey('Bookshelf', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'
        unique_together = (('book', 'bookshelf'),)
        verbose_name_plural = "bookshelf_mappings"


class Languages(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, related_name='languages_set')
    language = models.ForeignKey('Language', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_languages'
        unique_together = (('book', 'language'),)
        verbose_name_plural = "language_mappings"


class Subjects(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING, related_name='subjects_set')
    subject = models.ForeignKey('Subject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_subjects'
        unique_together = (('book', 'subject'),)
        verbose_name_plural = "subject_mappings"


class Bookshelf(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'books_bookshelf'
        verbose_name_plural = "bookshelves"


class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, models.DO_NOTHING, related_name='format_set')

    class Meta:
        managed = False
        db_table = 'books_format'
        verbose_name_plural = "formats"


class Language(models.Model):
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'books_language'
        verbose_name_plural = "languages"
        


class Subject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'books_subject'
        verbose_name_plural = "subjects"
