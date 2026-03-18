"""
Tests for consoles API v1.
"""

from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestConsolesListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/consoles/")
        assert response.status_code == 200

    def test_returns_console(self, api_client, console):
        data = api_client.get("/api/v1/consoles/").json()
        assert data["count"] >= 1

    def test_search_by_name(self, api_client, console):
        response = api_client.get("/api/v1/consoles/?search=NES")
        assert response.json()["count"] >= 1

    def test_filter_by_generation(self, api_client, console):
        response = api_client.get("/api/v1/consoles/?generation=3")
        assert response.json()["count"] >= 1

    def test_filter_by_type(self, api_client, console):
        response = api_client.get("/api/v1/consoles/?type=home")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestConsolesDetailEndpoint:
    def test_returns_200(self, api_client, console):
        response = api_client.get(f"/api/v1/consoles/{console.id}/")
        assert response.status_code == 200

    def test_returns_correct_console(self, api_client, console):
        response = api_client.get(f"/api/v1/consoles/{console.id}/")
        assert response.json()["name"] == "NES"
