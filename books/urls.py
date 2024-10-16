from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Initialize the router
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books', BookViewSet, basename='book')

# Include the generated URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
