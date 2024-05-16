from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
]
