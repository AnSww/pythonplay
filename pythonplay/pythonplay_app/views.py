from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = 'home.html'

class LetsgoPageView(TemplateView):
    template_name = 'letsgo.html'