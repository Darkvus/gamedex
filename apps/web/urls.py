from __future__ import annotations

from django.urls import path

from apps.web import views

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("collection/", views.collection, name="collection"),
    path("collection/<slug:slug>/", views.game_detail, name="game-detail"),
    path("api-explorer/", views.api_explorer, name="api-explorer"),
]
