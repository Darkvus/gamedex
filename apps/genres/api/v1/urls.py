"""
    URL configuration for genres API v1.
"""
from __future__ import annotations

from rest_framework.routers import DefaultRouter

from apps.genres.api.v1.views import GenreViewSet

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")
urlpatterns = router.urls
