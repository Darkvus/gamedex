"""
Development settings for gamedex.

Used for local development. Set DJANGO_SETTINGS_MODULE=config.settings.dev
"""

from __future__ import annotations

from config.settings.base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [  # type: ignore[name-defined]  # noqa: F405
    *INSTALLED_APPS,  # noqa: F405
    "debug_toolbar",
]

MIDDLEWARE = [  # type: ignore[name-defined]  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    *MIDDLEWARE,  # noqa: F405
]

INTERNAL_IPS = ["127.0.0.1"]
