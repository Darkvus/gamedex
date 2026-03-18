"""
Tests for genres API v1.
"""

from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestGenresListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/genres/")
        assert response.status_code == 200

    def test_returns_genre(self, api_client, genre):
        data = api_client.get("/api/v1/genres/").json()
        assert data["count"] >= 1

    def test_search(self, api_client, genre):
        response = api_client.get("/api/v1/genres/?search=Action")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestGenresDetailEndpoint:
    def test_returns_200(self, api_client, genre):
        response = api_client.get(f"/api/v1/genres/{genre.id}/")
        assert response.status_code == 200

    def test_returns_404(self, api_client):
        response = api_client.get("/api/v1/genres/00000000-0000-0000-0000-000000000000/")
        assert response.status_code == 404
