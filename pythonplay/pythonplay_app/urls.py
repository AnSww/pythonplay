from django.urls import path
from .views import HomePageView, LetsgoPageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('/letsgo', LetsgoPageView.as_view(), name='letsgo'),
)
