from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q

class BookPagination(PageNumberPagination):
    page_size = 25

@api_view(['GET'])
def book_list(request):
    query_params = request.query_params

    # Base query
    queryset = Book.objects.all()

    # Filter by book ID
    if 'gutenberg_id' in query_params:
        queryset = queryset.filter(gutenberg_id__in=query_params.getlist('gutenberg_id'))

    # Filter by language
    if 'language' in query_params:
        queryset = queryset.filter(languages__code__in=query_params.getlist('language'))

    # Filter by mime-type (download format)
    if 'mime_type' in query_params:
        queryset = queryset.filter(format__mime_type__in=query_params.getlist('mime_type'))

    # Filter by subject/topic
    if 'topic' in query_params:
        topic = query_params['topic']
        queryset = queryset.filter(Q(subjects__name__icontains=topic) | Q(bookshelves__name__icontains=topic))

    # Filter by author
    if 'author' in query_params:
        queryset = queryset.filter(authors_set__author__name__icontains=query_params['author'])

    # Filter by title
    if 'title' in query_params:
        queryset = queryset.filter(title__icontains=query_params['title'])

    # Sort by download count
    queryset = queryset.order_by('-download_count')

    # Paginate
    paginator = BookPagination()
    paginated_books = paginator.paginate_queryset(queryset, request)

    # Serialize and return
    serializer = BookSerializer(paginated_books, many=True)
    return paginator.get_paginated_response(serializer.data)
