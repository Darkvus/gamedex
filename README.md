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

### Games

```
GET /games
GET /games/{id}
GET /games/{id}/consoles
GET /games/{id}/releases
GET /games/{id}/franchise
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

### Consoles

```
GET /consoles
GET /consoles/{id}
GET /consoles/{id}/games
```

---

### Companies

```
GET /companies
GET /companies/{id}
GET /companies/{id}/games
```

---

### Genres

```
GET /genres
GET /genres/{id}
GET /genres/{id}/games
```

---

### Franchises

```
GET /franchises
GET /franchises/{id}
GET /franchises/{id}/games
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/Darkvus/gamedex.git
cd gamedex
```

Install dependencies with uv:

```bash
uv sync
```

Copy env file:

```bash
cp .env.example .env
```

Run migrations:

```bash
uv run python manage.py migrate
```

Seed data:

```bash
uv run python manage.py seed_data
```

Run server:

```bash
uv run python manage.py runserver
```

---

## 🐳 Docker

```bash
docker-compose up --build
```

---

## 📂 Project Structure

```
gamedex
│
├── apps
│   ├── games
│   ├── consoles
│   ├── companies
│   ├── genres
│   ├── franchises
│   └── releases
│
├── config
│   └── settings
│       ├── base.py
│       └── dev.py
├── data
│   ├── seeds
│   └── importers
├── docs
├── docker
├── manage.py
├── pyproject.toml
├── docker-compose.yml
└── README.md
```

---

## 🗄️ Data Model

### Game

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| slug | SlugField |
| description | TextField |
| release_year | IntegerField |
| genre_id | FK → Genre |
| franchise_id | FK → Franchise |
| developer_id | FK → Company |
| publisher_id | FK → Company |

---

### Console

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| manufacturer | CharField |
| release_year | IntegerField |
| generation | IntegerField |
| type | CharField |

---

### Company

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| country | CharField |
| founded | IntegerField |
| website | URLField |

---

### Genre

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| description | TextField |

---

### Franchise

| Field | Type |
|-------|------|
| id | BigAutoField |
| name | CharField |
| description | TextField |

---

### Release

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
-   factory_boy

Run tests:

```bash
uv run pytest
```

---

## 🗺️ Roadmap

### v1

-   games
-   consoles
-   companies
-   genres
-   franchises

### v2

-   characters
-   game engines
-   digital stores
-   sales data

### v3

-   ratings
-   reviews
-   screenshots
-   trailers

---

## 🤝 Contributing

Contributions are welcome.

1.  Fork repository
2.  Create branch
3.  Commit changes
4.  Open Pull Request

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
