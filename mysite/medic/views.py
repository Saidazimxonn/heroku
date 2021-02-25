from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, View, ListView
from .helpers import create_patient, create_message, create_email
from .models import (
    Patient,
    Doctor,

)

class PatientCreateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        doctors = Doctor.objects.all()
        context['doctors'] = doctors
        return context
    # def get_context_data(self, **kwargs):
    #     context = super(PatientCreateView, self).get_context_data(**kwargs)
    #     doc = Doctor.objects.all()
    #     context['doc'] = doc
    #     return context

class ActionView(View):

    def post(self, request):
        post_request = request.POST
        print(post_request.get('action', None))
        actions = {
            'create_patient': create_patient,
            'create_message': create_message,
            'create_email' : create_email,
            
        }
        actions[self.request.POST.get('action', None)](post_request)
        return redirect('/')
   

# class DoctorListView(ListView):

#     model  = Doctor
#     template_name = 'base.html'

#     def get_context_data(self, **kwargs):
#         context = super(DoctorListView, self).get_context_data(**kwargs)
#         doc = Doctor.objects.all()
#         context['doc'] = doc
#         return context

        
