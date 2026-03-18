"""
URL configuration for franchises API v1.
"""

from __future__ import annotations

from rest_framework.routers import DefaultRouter

from apps.franchises.api.v1.views import FranchiseViewSet

router = DefaultRouter()
router.register(r"franchises", FranchiseViewSet, basename="franchise")

urlpatterns = router.urls
