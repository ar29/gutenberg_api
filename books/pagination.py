# pagination.py
from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 25  # Default number of books per page
    page_size_query_param = 'page_size'  # Allow clients to set the page size
    max_page_size = 100  # Maximum limit for page size
