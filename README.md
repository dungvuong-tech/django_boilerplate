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

## Project Structure

```
your-project-name/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .envs/
│   ├── .production/
│   │   ├── .django
│   │   └── .postgres
│   ├── .development/
│   │   ├── .django
│   │   └── .postgres
│   └── .testing/
│       ├── .django
│       └── .postgres
├── .envs.example/
│   ├── .production/
│   │   ├── .django
│   │   └── .postgres
│   ├── .development/
│   │   ├── .django
│   │   └── .postgres
│   └── .testing/
│       ├── .django
│       └── .postgres
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
│
└── src/
    ├── apps/
    │   ├── __init__.py
    │   └── users/
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── models.py
    │       ├── serializers.py
    │       ├── tests/
    │       │   └── ...
    │       └── views.py
    │
    └── config/
        ├── __init__.py
        ├── asgi.py
        ├── settings/
        │   ├── __init__.py
        │   ├── base.py
        │   ├── development.py
        │   ├── production.py
        │   └── testing.py
        ��── urls.py
        └── wsgi.py
```

## Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd ltc-django-boilerplate
    ```

2.  **Copy the example environment variables:**
    ```bash
    cp -r .envs.example/ .envs/
    ```

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

The application will be available at `http://localhost:8000`.

## Environment Differences Explained

*   **Development:**
    *   **Purpose:** For local development and testing.
    *   **Database:** PostgreSQL running in a Docker container.
    *   **Settings:** `config.settings.development`
*   **Testing:**
    *   **Purpose:** For running automated tests.
    *   **Database:** In-memory SQLite for speed.
    *   **Settings:** `config.settings.testing`
*   **Production:**
    *   **Purpose:** For live deployment.
    *   **Database:** PostgreSQL, with connection details provided via environment variables.
    *   **Settings:** `config.settings.production`

## Adding a New Django App

1.  Create a new directory for your app in `src/apps/`.
2.  Add the app to the `LOCAL_APPS` list in `src/config/settings/base.py`.
3.  Run `docker-compose exec web python src/manage.py makemigrations` and `docker-compose exec web python src/manage.py migrate` to create the necessary database tables.

## Running Commands

*   **Run tests:**
    ```bash
    docker-compose exec web pytest
    ```

*   **Run linter:**
    ```bash
    docker-compose exec web ruff check .
    ```

*   **Run formatter:**
    ```bash
    docker-compose exec web ruff format .
    ```

*   **Run migrations:**
    ```bash
    docker-compose exec web python src/manage.py makemigrations
    docker-compose exec web python src/manage.py migrate
    ```

*   **Create a superuser:**
    ```bash
    docker-compose exec web python src/manage.py createsuperuser
    ```

## Deployment

This boilerplate is designed to be deployed using Docker. You can use any container orchestration platform like Kubernetes or Docker Swarm.

1.  Set up your production environment variables in `.envs/.production/.django` and `.envs/.production/.postgres`.
2.  Build the Docker image.
3.  Push the image to a container registry.
4.  Deploy the image to your hosting provider.
