from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.franchises.infrastructure.models import Franchises


@register(Franchises)
class FranchisesTranslationOptions(TranslationOptions):
    fields = ("name", "description")
