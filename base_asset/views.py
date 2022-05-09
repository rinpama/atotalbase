from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document
from .forms import DocumentForm


class DocumentCreateView(CreateView):
    model = Document
    # fields = ['upload', ]
    fields='__all__'
    success_url = reverse_lazy('base:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context
