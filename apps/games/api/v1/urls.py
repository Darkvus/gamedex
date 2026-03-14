"""
    URL configuration for games API v1.
"""
from __future__ import annotations

from rest_framework.routers import DefaultRouter

from apps.games.api.v1.views import GameViewSet

router = DefaultRouter()
router.register(r"games", GameViewSet, basename="game")
urlpatterns = router.urls
