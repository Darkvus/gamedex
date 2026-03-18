from __future__ import annotations

from django.urls import URLPattern
from rest_framework.routers import DefaultRouter

from apps.regions.api.v1.views import RegionViewSet

router = DefaultRouter()
router.register(r"regions", RegionViewSet, basename="region")
urlpatterns: list[URLPattern] = router.urls
