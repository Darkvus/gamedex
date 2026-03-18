from __future__ import annotations

from django.contrib import admin

from apps.franchises.infrastructure.models import Franchises


@admin.register(Franchises)
class FranchisesAdmin(admin.ModelAdmin):
    list_display = ("name", "founded_year", "games_count")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def games_count(self, obj: Franchises) -> int:
        return obj.games.count()
    games_count.short_description = "Games"
