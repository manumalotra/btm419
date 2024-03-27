from django.urls import path
from . import views

app_name = 'reports_app'

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
]
