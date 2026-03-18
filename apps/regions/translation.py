from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.regions.infrastructure.models import Regions


@register(Regions)
class RegionsTranslationOptions(TranslationOptions):
    fields = ("name",)
