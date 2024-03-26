from django.urls import path
from . import views

app_name = 'sales_app'

urlpatterns = [
    # Home page
    path('', views.sales_homepage, name='sales_homepage'),
    path('add/', views.add_sale, name='add_sale'),
]