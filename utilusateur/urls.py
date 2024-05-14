from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from utilusateur.views import UserProfile, EditProfile
from .views import logout_view

urlpatterns = [
    # Profile Section
    path('profile/', UserProfile, name="profile"),
    path('profile/edit/', EditProfile, name="editprofile"),

    # User Authentication
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name='login'),

    path('register/', views.register, name='register'),
]
