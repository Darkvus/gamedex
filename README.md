# 🎮 GameDex

### The Open Video Game Data API

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)]()
[![Django](https://img.shields.io/badge/django-5.x-green)]()
[![API](https://img.shields.io/badge/API-REST-orange)]()

GameDex is an **open-source API for video game data**.

Inspired by projects like PokéAPI, GameDex provides structured
information about:

-   🎮 Video games
-   🕹️ Consoles
-   🏢 Companies
-   📦 Releases
-   🧩 Genres
-   🌍 Regions
-   🏷️ Franchises

The goal is to create the **largest open database of video game
information for developers.**

---

## 📚 Table of Contents

-   [Overview](#-overview)
-   [Features](#-features)
-   [Architecture](#-architecture)
-   [API Resources](#-api-resources)
-   [Installation](#-installation)
-   [Running the API](#-docker)
-   [Project Structure](#-project-structure)
-   [Data Model](#-data-model)
-   [Roadmap](#-roadmap)
-   [Contributing](#-contributing)
-   [License](#-license)

---

## 🌍 Overview

GameDex provides a **public REST API** for accessing structured
information about the history of video games.

Developers can use it to build:

-   gaming apps
-   dashboards
-   bots
-   retro tools
-   educational projects

---

## ✨ Features

-   REST API
-   OpenAPI documentation
-   Docker ready
-   PostgreSQL database
-   Redis caching
-   Fully open dataset
-   Community contributions

---

## 🏗️ Architecture

```
Clients → API Gateway → GameDex API → PostgreSQL
```

Services:

-   Games
-   Consoles
-   Companies
-   Genres
-   Franchises
-   Releases

---

## 🧩 API Resources

> ✅ = Available now &nbsp;|&nbsp; 🔜 = Planned

### Games ✅

```
GET /api/v1/games/
GET /api/v1/games/{id}/
```

Example:

```json
{
  "id": 1,
  "name": "Super Mario Bros",
  "release_year": 1985,
  "genre": "Platform",
  "developer": "Nintendo"
}
```

---

### Consoles ✅

```
GET /api/v1/consoles/
GET /api/v1/consoles/{id}/
```

---

### Companies ✅

```
GET /api/v1/companies/
GET /api/v1/companies/{id}/
```

---

### Genres ✅

```
GET /api/v1/genres/
GET /api/v1/genres/{id}/
```

---

### Franchises 🔜

```
GET /api/v1/franchises/
GET /api/v1/franchises/{id}/
GET /api/v1/franchises/{id}/games/
```

---

### Releases 🔜

```
GET /api/v1/releases/
GET /api/v1/releases/{id}/
```

---

## 🚀 Installation

### With Docker Compose (recommended)

```bash
git clone https://github.com/Darkvus/gamedex.git
cd gamedex
cp .env.example .env
docker compose up --build
```

API available at `http://localhost:8000`.

### Local development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/Darkvus/gamedex.git
cd gamedex
uv sync
cp .env.example .env
DJANGO_SETTINGS_MODULE=config.settings.dev uv run python manage.py migrate
DJANGO_SETTINGS_MODULE=config.settings.dev uv run python manage.py runserver
```

---

## 📂 Project Structure

```
gamedex
│
├── apps
│   ├── games         ✅
│   ├── consoles      ✅
│   ├── companies     ✅
│   ├── genres        ✅
│   ├── franchises    🔜
│   └── releases      🔜
│
├── config
│   └── settings
│       ├── base.py
│       └── dev.py
├── manage.py
├── pyproject.toml
├── docker-compose.yml
└── README.md
```

Each domain module follows Clean Architecture:

```
apps/<domain>/
├── domain/           # Entities, value objects, aggregates, repository interfaces
├── application/
│   ├── use_cases/    # Orchestration + DTOs
│   └── services/     # Business logic + DTOs
├── infrastructure/
│   ├── models.py     # Django ORM
│   └── repositories/ # Repository implementations
├── api/v1/           # Serializers, views, URLs
└── migrations/
```

---

## 🗄️ Data Model

### Game ✅

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| slug | SlugField |
| description | TextField |
| release_year | IntegerField |
| genre_id | FK → Genre |
| franchise_id | FK → Franchise 🔜 |
| developer_id | FK → Company |
| publisher_id | FK → Company |

---

### Console ✅

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| manufacturer | CharField |
| release_year | IntegerField |
| generation | IntegerField |
| type | CharField |

---

### Company ✅

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| country | CharField |
| founded | IntegerField |
| website | URLField |

---

### Genre ✅

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| description | TextField |

---

### Franchise 🔜

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| description | TextField |

---

### Release 🔜

| Field | Type |
|-------|------|
| id | BigAutoField |
| game_id | FK → Game |
| console_id | FK → Console |
| region | CharField |
| release_date | DateField |

---

## 📊 Pagination

```
GET /games?limit=20&offset=0
```

Example response:

```json
{
  "count": 12000,
  "next": "/games?limit=20&offset=20",
  "results": []
}
```

---

## 📖 API Documentation

Interactive docs available at:

- `/docs` — Swagger UI
- `/redoc` — ReDoc
- `/schema` — OpenAPI schema

---

## 📦 SDKs

Planned SDKs:

-   gamedex-js
-   gamedex-python
-   gamedex-go
-   gamedex-rust

---

## 🧪 Testing

Testing stack:

-   pytest
-   pytest-django
-   pytest-mock
-   pytest-cov

Run tests:

```bash
uv run pytest
uv run pytest --cov=apps
```

---

## 🗺️ Roadmap

### v1 — Core catalog ✅ / 🔜

- [x] Games
- [x] Consoles
- [x] Companies
- [x] Genres
- [ ] Franchises
- [ ] Releases

### v2 — Extended data

- [ ] Characters
- [ ] Game engines
- [ ] Digital stores
- [ ] Sales data

### v3 — Community

- [ ] Ratings & reviews
- [ ] Screenshots
- [ ] Trailers

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit following [Conventional Commits](https://www.conventionalcommits.org/)
4. Run tests and linting before pushing:
   ```bash
   uv run ruff check .
   uv run pytest
   ```
5. Open a Pull Request

---

## 📜 License

MIT License

Dataset: Open Database License (ODbL)

---

## ⭐ Support

If you like the project:

⭐ Star the repository
🐛 Report issues
🤝 Contribute

---

## ❤️ GameDex

Open Video Game Knowledge for Developers.
