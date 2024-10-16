# books/tests/test_views.py

import requests
from django.test import TestCase
from django.urls import reverse

class BookAPITestCase(TestCase):
    # URL for the API endpoint
    API_URL = reverse('book-list')  # Replace with your actual URL name

    def setUp(self):
        # You can set up any necessary variables or configurations here.
        self.base_url = 'http://127.0.0.1:8000'  # Adjust according to your local settings

    def test_get_books(self):
        """Test the GET method on the /api/books/ endpoint."""

        # Make the GET request
        response = requests.get(f'{self.base_url}{self.API_URL}')

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check that the response contains a list of books
        json_response = response.json()["results"]
        self.assertIsInstance(json_response, list)  # The response should be a list

        # You can also check for the structure of the first book in the list if available
        if json_response:  # If there are any books returned
            book = json_response[0]
            self.assertIn('title', book)
            self.assertIn('author', book)
            self.assertIn('languages', book)
            self.assertIn('subjects', book)
            self.assertIn('bookshelves', book)
            self.assertIn('download_links', book)

    def test_get_books_with_query_params(self):
        """Test the GET method on the /api/books/ endpoint with query parameters."""

        # Define query parameters
        query_params = {
            'language': 'en',
            'topic': 'child',
        }

        # Make the GET request
        response = requests.get(f'{self.base_url}{self.API_URL}', params=query_params)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check that the response contains a list of books
        json_response = response.json()["results"]
        self.assertIsInstance(json_response, list)  # The response should be a list

        # Check that the returned books match the filter criteria
        for book in json_response:
            # Assert that each book contains the specified language or topic in its details
            # You might want to implement actual checks based on your data
            self.assertIn({'code': 'en'}, book['languages'])  # Adjust according to your API's response structure

    def test_get_books_no_results(self):
        """Test the GET method on the /api/books/ endpoint with parameters that yield no results."""

        # Define a query parameter that is unlikely to return results
        query_params = {
            'language': 'invalid_language_code',
        }

        # Make the GET request
        response = requests.get(f'{self.base_url}{self.API_URL}', params=query_params)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check that the response is an empty list
        json_response = response.json()
        self.assertEqual(json_response, {'count': 0, 'next': None, 'previous': None, 'results': []})  # Expecting an empty list

