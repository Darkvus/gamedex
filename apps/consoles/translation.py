from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.consoles.infrastructure.models import Consoles


@register(Consoles)
class ConsolesTranslationOptions(TranslationOptions):
    fields = ("name",)
