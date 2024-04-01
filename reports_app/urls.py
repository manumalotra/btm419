from django.urls import path
from . import views

app_name = 'reports_app'

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
    path('sales/', views.sales_report, name='sales_report'),
    path('claims/', views.claims_report, name='claims_report'),
]
