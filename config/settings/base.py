"""
    Base settings for gamedex.

    Used for deployment. Set DJANGO_SETTINGS_MODULE=config.settings.base
"""
from __future__ import annotations

from pyms_django.settings.main import *  # noqa: F401,F403

SERVICE_NAME = "gamedex"
BASE_PATH = ""
MULTITENANT = False

INSTALLED_APPS = [  # type: ignore[name-defined]  # noqa: F405
    *INSTALLED_APPS,
    "apps.games",
    "apps.consoles",
    "apps.companies",
    "apps.genres",
    "apps.franchises",
    "apps.releases",
]

LOCAL_APPS: list[tuple[str, str]] = [
    ("apps.games.api.v1.urls", BASE_PATH),
    ("apps.consoles.api.v1.urls", BASE_PATH),
    ("apps.companies.api.v1.urls", BASE_PATH),
    ("apps.genres.api.v1.urls", BASE_PATH),
    ("apps.franchises.api.v1.urls", BASE_PATH),
    ("apps.releases.api.v1.urls", BASE_PATH),
]
