# GameDex — Claude Context

## Project
REST API de catalogo de videojuegos. Django 5.2 + DRF via `pyms-django-chassis`. Python 3.11+. Gestion de dependencias con `uv`.

## Architecture
Clean Architecture / DDD por app:
```
apps/<domain>/
  domain/          # entities, value_objects, aggregates, repositories (interfaces)
  application/
    use_cases/     # orquestacion, dtos
    services/      # logica de negocio, dtos
  infrastructure/
    models.py      # Django ORM
    repositories/  # implementaciones
    services/
  api/v1/          # serializers, views, urls
  migrations/
```

## Apps
- `games` — videojuegos
- `consoles` — consolas
- `companies` — empresas/publishers/developers
- `genres` — generos

## Stack
- Django 5.2, DRF (via pyms-django-chassis), gunicorn
- uv (lock file: uv.lock), hatchling build
- Ruff (linter+formatter), pre-commit
- pytest, pytest-django, pytest-mock, pytest-cov
- Docker multi-stage (builder=uv sync, runtime=gunicorn)
- Settings: `config.settings.dev` (DEBUG=True), base via `pyms_django`

## URLs
Montadas via `pyms_django.urls.urlpatterns`. Cada app registra sus propias rutas en `api/v1/urls.py`.

## Key conventions
- `from __future__ import annotations` en todos los modulos
- Ruff config en `ruff.toml`
- No mocks en tests de repositorios — usar DB real
- Respuestas cortas y directas, sin trailing summaries
