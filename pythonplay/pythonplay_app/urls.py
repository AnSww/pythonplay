from django.urls import path
from .views import HomePageView, LetsgoPageView, LoginPageView, RoadmapPageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('letsgo', LetsgoPageView.as_view(), name='letsgo'),
    path('login', LoginPageView.as_view(), name='login'),
    path('roadmap', RoadmapPageView.as_view(), name='roadmap'),
)
