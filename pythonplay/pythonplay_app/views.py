from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



class HomePageView(TemplateView):
    template_name = 'home.html'

class LetsgoPageView(TemplateView):
    template_name = 'letsgo.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class RoadmapPageView(TemplateView):
    template_name = 'roadmap.html'

