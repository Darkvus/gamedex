"""
Base settings for gamedex.
Used for deployment. Set DJANGO_SETTINGS_MODULE=config.settings.base
"""

from __future__ import annotations

from pathlib import Path

from django.utils.translation import gettext_lazy as _
from pyms_django.settings.main import *  # noqa: F401,F403

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SERVICE_NAME = "gamedex"
BASE_PATH = ""
MULTITENANT = False

ROOT_URLCONF = "config.urls"

USE_I18N = True
LANGUAGE_CODE = "en"
LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
MODELTRANSLATION_FALLBACK_LANGUAGES = ("en",)

INSTALLED_APPS = [  # type: ignore[name-defined]  # noqa: F405
    "modeltranslation",
    "django.contrib.admin",
    *INSTALLED_APPS,  # noqa: F405
    "apps.games",
    "apps.consoles",
    "apps.companies",
    "apps.genres",
    "apps.regions",
    "apps.releases",
    "apps.franchises",
    "inertia",
    "django_vite",
    "apps.web",
]

LOCAL_APPS: list[tuple[str, str]] = [
    ("apps.games.api.v1.urls", BASE_PATH),
    ("apps.consoles.api.v1.urls", BASE_PATH),
    ("apps.companies.api.v1.urls", BASE_PATH),
    ("apps.genres.api.v1.urls", BASE_PATH),
    ("apps.regions.api.v1.urls", BASE_PATH),
    ("apps.releases.api.v1.urls", BASE_PATH),
]

MIDDLEWARE = [  # type: ignore[name-defined]  # noqa: F405
    *MIDDLEWARE,  # noqa: F405
    "django.middleware.locale.LocaleMiddleware",
    "inertia.middleware.InertiaMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

INERTIA_LAYOUT = "base.html"

DJANGO_VITE = {
    "default": {
        "dev_mode": True,
        "dev_server_port": 5173,
    },
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "frontend" / "dist"]
