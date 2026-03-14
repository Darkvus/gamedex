from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.genres.infrastructure.models import Genres


@register(Genres)
class GenresTranslationOptions(TranslationOptions):
    fields = ("name", "description")
