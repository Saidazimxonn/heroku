from django.urls import path
from .views import PatientCreateView, ActionView

urlpatterns = [

    path('', PatientCreateView.as_view(), name='home'),
    path('action/', ActionView.as_view(), name='action_view')
]
