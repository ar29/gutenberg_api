# Django Gutenberg API

This project is a Django-based REST API that allows users to retrieve books from a Project Gutenberg-like database, applying filters such as language, author, title, topic, and more. The API supports pagination and returns book data in JSON format.

## Table of Contents

1. [Technologies](#technologies)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation and Setup](#installation-and-setup)
5. [Running the Project](#running-the-project)
6. [Running Tests](#running-tests)
7. [Environment Variables](#environment-variables)

## Technologies

- Django
- Django Rest Framework
- PostgreSQL
- Docker & Docker Compose
- Swagger UI
- dj-database-url

## Features

- Retrieve books with various filters (author, title, topic, language, mime-type).
- Pagination support (25 books per page).
- Sorting by download count.
- Swagger UI integration for API exploration.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Docker
- Docker Compose

## Installation and Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/django-gutenberg-api.git
    cd django-gutenberg-api
    ```

## Running the Project

1. **Using Docker Compose**

    To run the project locally using Docker Compose, run the following commands:

    ```bash
    docker-compose -f docker-compose.dev.yml up --build
    ```

    This will build and start the project with PostgreSQL as the database.

2. **Accessing the API**

    Once the app is running, you can access the API at:

    ```
    http://localhost:8000/api/
    ```

3. **Swagger UI**

    The API documentation is available at:

    ```
    http://localhost:8000/swagger/
    ```

## Running Tests

1. **Using `Docker`**

    The test suite uses `docker`. To run the test suite, use the following command:

    ```bash
    docker exec -it gutenberg_api-web-1 python manage.py test     
    ```

## Environment Variables

The following environment variables need to be set for the project to work correctly:

- `DEBUG`: Set to `1` for development mode.
- `SECRET_KEY`: The Django secret key.
- `DATABASE_URL`: The PostgreSQL database url.

Make sure to configure these values in the `.env` file as needed.