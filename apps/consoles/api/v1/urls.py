"""
    URL configuration for consoles API v1.
"""
from __future__ import annotations

from rest_framework.routers import DefaultRouter

from apps.consoles.api.v1.views import ConsoleViewSet

router = DefaultRouter()
router.register(r"consoles", ConsoleViewSet, basename="console")
urlpatterns = router.urls
