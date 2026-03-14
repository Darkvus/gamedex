"""
    Base settings for gamedex.
    Used for deployment. Set DJANGO_SETTINGS_MODULE=config.settings.base
"""
from __future__ import annotations

from django.utils.translation import gettext_lazy as _
from pyms_django.settings.main import *  # noqa: F401,F403

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
    *INSTALLED_APPS,
    "apps.games",
    "apps.consoles",
    "apps.companies",
    "apps.genres",
    "apps.regions",
    "apps.releases",
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
    *MIDDLEWARE,
    "django.middleware.locale.LocaleMiddleware",
]
