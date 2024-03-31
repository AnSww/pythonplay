from django.urls import path
from .views import HomePageView, LetsgoPageView, LoginPageView, RoadmapPageView,  Level_0_View

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('letsgo', LetsgoPageView.as_view(), name='letsgo'),
    path('login', LoginPageView.as_view(), name='login'),
    path('roadmap', RoadmapPageView.as_view(), name='roadmap'),
    path('level0/', Level_0_View.as_view(), name='level0'),
)
