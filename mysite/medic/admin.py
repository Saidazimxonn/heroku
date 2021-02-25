from django.contrib import admin
from django.db import models
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from .models import (
    Patient,
    Doctor,
    Message,
    Email,
)
# Register your models here.

# class MovieAdminForm(forms.ModelForm):

#     description_ru = forms.CharField(lambda="Описание", widget=CKEditorUploadingWidget())
#     description_uz = forms.CharField(lambda="Ma\'lumot", widget=CKEditorUploadingWidget())

#     class Meta:
#         models



class PatientAdmin(TranslationAdmin):
    list_display = (
        'name', 'phone', 'email', 'day', 'time', 'doctor', 'message'
    )
    list_filter = (
        'day', 'doctor','time'
    )
    list_display_links =(
         'name', 'phone', 'email', 'day', 'time', 'doctor', 'message'
    )




class MessageAdmin(TranslationAdmin):
    list_display = (
          'name', 'email', 'phone', 'subject', 'message'
    )
    list_display_links = (
          'name', 'email', 'phone', 'subject', 'message'
    )
    list_filter = (
        'name', 'subject'
    )
class DoctorAdmin(TranslationAdmin):
    list_display = (
        'name', 'specialist')
    list_display_links = (
         'name', 'specialist'
    )
    list_filter = (
        'specialist', 'name'
    )
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Email)
