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

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

def create_level_view(level_number):
    class_name = f"Level_{level_number}_View"
    template_name = f"level{level_number}.html"

    # Создание класса динамически с помощью type()
    dynamic_class = type(
        class_name,
        (TemplateView,),
        {'template_name': template_name}
    )

    return dynamic_class

Level_0_View = create_level_view(0)
Level_1_View = create_level_view(1)