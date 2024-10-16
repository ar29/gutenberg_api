import django_filters
from .models import Book
from django.db.models import Q

class BookFilter(django_filters.FilterSet):
    gutenberg_id = django_filters.BaseInFilter(field_name='gutenberg_id', lookup_expr='in')
    author = django_filters.CharFilter(field_name='authors_set__author__name', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    language = django_filters.CharFilter(method='filter_language', label="Language") # Supports multiple values
    topic = django_filters.CharFilter(method='filter_topic', label="Topic")  # Custom method for topic filtering
    mime_type = django_filters.CharFilter(method='filter_mime_type', label="Mime Type")  # Custom method for mime type filtering

    class Meta:
        model = Book
        fields = ['gutenberg_id', 'author', 'title', 'language', 'mime_type', 'topic']


    def filter_language(self, queryset, name, value):
        # Split the input into a list of languages
        languages = value.split(',')
        # Use Q objects to filter the queryset for each language
        query = Q()
        for lang in languages:
            query |= Q(languages_set__language__code__iexact=lang.strip())
        # Return the filtered queryset
        return queryset.filter(query).distinct()
    
    def filter_topic(self, queryset, name, value):
        if value:
            topics = [x.strip() for x in value.split(',')]
            query = queryset.none()
            for topic in topics:
                # Add filters for both subjects and bookshelves
                query |= queryset.filter(subjects_set__subject__name__icontains=topic)
                query |= queryset.filter(bookshelves_set__bookshelf__name__icontains=topic)
            return query.distinct()  # Return unique results
        return queryset

    def filter_mime_type(self, queryset, name, value):
        # Split the input into a list of mime types
        mime_types = value.split(',')
        # Use Q objects to filter the queryset for each mime type
        query = Q()
        for mime in mime_types:
            query |= Q(format_set__mime_type__icontains=mime.strip())
        return queryset.filter(query).distinct()
