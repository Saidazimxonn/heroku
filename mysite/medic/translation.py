from modeltranslation import fields
from modeltranslation.translator import register, TranslationOptions
from .models import (
    Doctor,
    Message,
    Patient,

)


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'specialist',
        'info'

    )

@register(Patient)
class PatientTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'message'
    )

@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'subject',
        'message'
    )