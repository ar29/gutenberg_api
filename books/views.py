from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from .pagination import BookPagination

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.exclude(download_count__isnull=True).prefetch_related(
        'authors_set__author',        # Prefetch related authors
        'languages_set__language',    # Prefetch related languages
        'subjects_set__subject',      # Prefetch related subjects
        'bookshelves_set__bookshelf'   # Prefetch related bookshelves
    ).order_by('-download_count')      # Order by download count

    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['download_count']
    pagination_class = BookPagination  # Pagination to limit to 25 books per page
