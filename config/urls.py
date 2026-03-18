from __future__ import annotations

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from pyms_django.urls import urlpatterns as pyms_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.web.urls")),
] + pyms_urlpatterns + i18n_patterns(
    path("api/v1/", include("apps.genres.api.v1.urls")),
    path("api/v1/", include("apps.companies.api.v1.urls")),
    path("api/v1/", include("apps.consoles.api.v1.urls")),
    path("api/v1/", include("apps.games.api.v1.urls")),
    path("api/v1/", include("apps.regions.api.v1.urls")),
    path("api/v1/", include("apps.releases.api.v1.urls")),
    path("api/v1/", include("apps.franchises.api.v1.urls")),
    prefix_default_language=False,
)
