# LTC Django Boilerplate

A comprehensive, production-ready Django boilerplate project managed by Poetry. This boilerplate is designed to be modular, well-documented, and incorporates modern best practices for structure, security, testing, CI/CD, and deployment using Docker.

## Features

*   **Core Technologies:** Python 3.11, Django 5.0, PostgreSQL.
*   **Dependency Management:** Poetry for clear, deterministic dependency management.
*   **Containerization:** Multi-stage Dockerfile for production and a `docker-compose.yml` for local development.
*   **Split Settings:** Environment-specific settings for development, testing, and production using `django-environ`.
*   **Custom User Model:** A custom User model with email as the username field.
*   **API Support:** Django Rest Framework (DRF) with JWT authentication.
*   **Code Quality:** `ruff` for linting and formatting, with pre-commit hooks.
*   **Testing:** `pytest` with `pytest-django` and `factory-boy`.
*   **CI/CD:** A basic CI/CD pipeline using GitHub Actions.
*   **Logging:** JSON-formatted logging for production.

## Project Setup Guide

This guide will walk you through setting up a new project from this boilerplate.

1.  **Clone the boilerplate:**
    ```bash
    git clone <repository-url> your-project-name
    cd your-project-name
    ```

2.  **Initialize Poetry and install dependencies:**
    This boilerplate uses Poetry for dependency management. To install the dependencies, run:
    ```bash
    poetry install
    ```

3.  **Set up pre-commit hooks:**
    This boilerplate uses `pre-commit` to run `ruff` for linting and formatting on every commit. To install the hooks, run:
    ```bash
    poetry run pre-commit install
    ```

4.  **Create environment variables:**
    Copy the example environment variables to create your own `.envs` directory:
    ```bash
    cp -r .envs.example/ .envs/
    ```
    Review and update the variables in the `.envs` files as needed.

5.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```
    This will start the Django development server and a PostgreSQL database. The application will be available at `http://localhost:8000`.

6.  **Run initial migrations and create a superuser:**
    ```bash
    docker-compose exec web python src/manage.py migrate
    docker-compose exec web python src/manage.py createsuperuser
    ```

7.  **Create a new Django app:**
    To create a new app, run the following command:
    ```bash
    docker-compose exec web python src/manage.py startapp my_app src/apps/my_app
    ```
    Then, add `'apps.my_app'` to the `LOCAL_APPS` list in `src/config/settings/base.py`.

## Testing Guide

This boilerplate uses `pytest` for testing. Here's a guide to get you started with writing tests.

### Writing Your First Test

1.  **Create a test file:**
    In your app's `tests` directory, create a new file starting with `test_`. For example, `test_models.py`.

2.  **Write a simple test:**
    Here's an example of a test for a model:
    ```python
    import pytest
    from .factories import YourModelFactory

    @pytest.mark.django_db
    def test_your_model_creation():
        instance = YourModelFactory()
        assert instance.pk is not None
    ```

### Using Factories

This boilerplate uses `factory-boy` to create test data. You can define factories for your models in a `factories.py` file in your app's directory.

```python
# src/apps/your_app/factories.py
import factory
from .models import YourModel

class YourModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = YourModel

    # Define your model's fields here
    name = factory.Faker("name")
```

### Running Tests

To run all tests, use the following command:
```bash
docker-compose exec web pytest
```

To run tests for a specific app:
```bash
docker-compose exec web pytest src/apps/your_app/
```

## Logging Guide

This boilerplate is configured to use JSON-formatted logging in production for easy parsing by log management systems.

### How to Use Logging

To log messages in your application, you can use Python's built-in `logging` module.

1.  **Get a logger instance:**
    In your `views.py` or any other file, get a logger instance:
    ```python
    import logging

    logger = logging.getLogger(__name__)
    ```

2.  **Log messages:**
    You can then use the logger to log messages at different levels:
    ```python
    def my_view(request):
        logger.debug("This is a debug message.")
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")
        logger.critical("This is a critical message.")
        # ... your view logic ...
    ```

### Log Levels

*   **DEBUG:** Detailed information, typically of interest only when diagnosing problems.
*   **INFO:** Confirmation that things are working as expected.
*   **WARNING:** An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
*   **ERROR:** Due to a more serious problem, the software has not been able to perform some function.
*   **CRITICAL:** A serious error, indicating that the program itself may be unable to continue running.

## Environment Differences Explained

*   **Development:**
    *   **Purpose:** For local development and testing.
    *   **Database:** PostgreSQL running in a Docker container.
    *   **Settings:** `config.settings.development`
*   **Testing:**
    *   **Purpose:** For running automated tests.
    *   **Database:** PostgreSQL running in a Docker container.
*   **Production:**
    *   **Purpose:** For live deployment.
    *   **Database:** PostgreSQL, with connection details provided via environment variables.
    *   **Settings:** `config.settings.production`

## Deployment

This boilerplate is designed to be deployed using Docker. You can use any container orchestration platform like Kubernetes or Docker Swarm.

1.  Set up your production environment variables in `.envs/.production/.django` and `.envs/.production/.postgres`.
2.  Build the Docker image.
3.  Push the image to a container registry.
4.  Deploy the image to your hosting provider.