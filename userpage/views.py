from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeSignedView(TemplateView):
    template_name = "userpage/home.html"