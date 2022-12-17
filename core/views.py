from django.shortcuts import render
from django.views.generic import ListView
from .models import NotSignedHome


class HomeListView(ListView):
    template_name = 'core/home.html'
    model = NotSignedHome
    context_object_name = 'home'

