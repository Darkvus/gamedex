from __future__ import annotations

from modeltranslation.translator import TranslationOptions, register

from apps.companies.infrastructure.models import Companies


@register(Companies)
class CompaniesTranslationOptions(TranslationOptions):
    fields = ("name",)
