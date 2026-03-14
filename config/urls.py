"""
    URL configuration.
"""
from __future__ import annotations

from django.contrib import admin
from django.urls import include, path
from pyms_django.urls import urlpatterns as pyms_urlpatterns

urlpatterns = pyms_urlpatterns + [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.genres.api.v1.urls")),
    path("api/v1/", include("apps.companies.api.v1.urls")),
    path("api/v1/", include("apps.consoles.api.v1.urls")),
    path("api/v1/", include("apps.games.api.v1.urls")),
]
