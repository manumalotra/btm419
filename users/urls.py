from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name="logout"),
]