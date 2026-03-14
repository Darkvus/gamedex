"""
    URL configuration for companies API v1.
"""
from __future__ import annotations

from rest_framework.routers import DefaultRouter

from apps.companies.api.v1.views import CompanyViewSet

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")
urlpatterns = router.urls
