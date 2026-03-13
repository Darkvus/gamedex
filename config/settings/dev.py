"""
    Development settings for gamedex.

    Used for local development. Set DJANGO_SETTINGS_MODULE=config.settings.dev
"""
from __future__ import annotations

from config.settings.base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ["*"]
