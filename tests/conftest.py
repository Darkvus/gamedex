"""
    Shared pytest fixtures for gamedex tests.
"""
from __future__ import annotations

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def genre(db):
    from apps.genres.infrastructure.models import Genres
    return Genres.objects.create(name="Action")


@pytest.fixture
def company(db):
    from apps.companies.infrastructure.models import Companies
    return Companies.objects.create(name="Nintendo", country="Japan", founded=1889)


@pytest.fixture
def console(db):
    from apps.consoles.infrastructure.models import Consoles
    return Consoles.objects.create(name="NES", manufacturer="Nintendo", release_year=1983, generation=3, type="home")


@pytest.fixture
def franchise(db):
    from apps.franchises.infrastructure.models import Franchises
    return Franchises.objects.create(name="Mario", description="Super Mario franchise", founded_year=1985)


@pytest.fixture
def game(db, genre, company, console, franchise):
    from apps.games.infrastructure.models import Games
    g = Games.objects.create(
        name="Super Mario Bros",
        description="Classic platformer",
        release_year=1985,
        genre=genre,
        developer=company,
        publisher=company,
        franchise=franchise,
    )
    g.consoles.add(console)
    return g


@pytest.fixture
def region(db):
    from apps.regions.infrastructure.models import Regions
    return Regions.objects.create(code="NA", name="North America")


@pytest.fixture
def release(db, game, region, console):
    from apps.releases.infrastructure.models import Releases
    from datetime import date
    return Releases.objects.create(game=game, region=region, console=console, release_date=date(1985, 10, 18))
