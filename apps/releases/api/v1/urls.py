from __future__ import annotations

from django.urls import URLPattern
from rest_framework.routers import DefaultRouter

from apps.releases.api.v1.views import ReleaseViewSet

router = DefaultRouter()
router.register(r"releases", ReleaseViewSet, basename="release")
urlpatterns: list[URLPattern] = router.urls
