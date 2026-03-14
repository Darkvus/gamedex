from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.games.infrastructure.models import Games


@register(Games)
class GamesTranslationOptions(TranslationOptions):
    fields = ("name", "description")
