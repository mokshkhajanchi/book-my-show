from .views import RegisterAPI, LoginAPI
from django.urls import path, include
from knox import views as knox_views

urlpatterns = [
    path('user/register/', RegisterAPI.as_view(), name='user-register'),
    path('user/login/', LoginAPI.as_view(), name='user-login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='user-logout'),
]