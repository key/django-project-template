# Django 4.2+ Project Template

This is a simple Django 4.2+ project template with a modern setup. Most Django project templates make too many assumptions or are overly complicated. This template makes minimal assumptions while providing a useful foundation for new projects.

## Features

- Django 4.2+ with Python 3.12 support
- Uses [Pipenv](https://github.com/pypa/pipenv) for dependency management
- REST API support with [Django REST Framework](https://www.django-rest-framework.org/)
- Development tools:
  - [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org) for debugging and performance insights
  - [django-extensions](http://django-extensions.readthedocs.org) for useful development commands
  - [pre-commit](https://pre-commit.com/) hooks for code quality
- Docker Compose setup for PostgreSQL and Redis
- GitHub Actions workflow for CI/CD
- HTTPS and security settings for staging and production
- PostgreSQL database support with psycopg2-binary
- Redis cache integration with django-redis
- Sentry integration for error tracking
- Bjoern WSGI server for high-performance request handling
- WhiteNoise for static file serving

## How to install

### Prerequisites

Install system requirements:

```bash
brew bundle  # On macOS
# For Ubuntu/Debian: sudo apt-get install -y libev-dev direnv
```

### Create a new project

Create a Django project from this template:

```bash
django-admin startproject \
  --template=https://github.com/key/django-project-template/archive/master.zip \
  --name=env.example \
  --extension=py,md,yml \
  project_name
```

### Setup environment

Create `.env` from `env.example` and allow direnv:

```bash
mv env.example .env
direnv allow .
```

### Install dependencies

Install Python modules:

```bash
# For macOS with Homebrew
C_INCLUDE_PATH=/usr/local/include LD_LIBRARY_PATH=/usr/local/lib pipenv install --dev

# For Ubuntu/Debian
pipenv install --dev
```

### Start development services

Start PostgreSQL and Redis using Docker:

```bash
docker compose up -d
```

## Environment variables

This template uses [django-configurations](https://django-configurations.readthedocs.io/) for class-based settings. The `DJANGO_CONFIGURATION` environment variable determines which settings class to use.

### Common environment variables

These variables are used in all environments:

```
DJANGO_CONFIGURATION=Dev  # Options: Dev, Test, Prod
DJANGO_SECRET_KEY='your-secret-key'
DATABASE_URL='postgresql://postgres:password@localhost:15432/project_name'
CACHE_URL='redis://localhost:16379/1'
```

### Production environment variables

These settings are used in staging and production environments:

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
SENTRY_DSN='your-sentry-dsn'  # For error tracking
```

## Development

### Running the server

Start the Django development server:

```bash
python manage.py runserver
```

### Running tests

Run tests with:

```bash
python manage.py test --configuration=Test
```

## Deployment

This template can be deployed to various platforms:

1. **Self-hosted server**: Use the built-in Bjoern WSGI server for high performance
2. **Docker**: The template is Docker-ready with the included compose.yaml
3. **Cloud platforms**: Compatible with most cloud platforms that support Django

## License

The MIT License (MIT)

Copyright (c) 2012-2025 José Padilla, Mitsukuni Sato

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
