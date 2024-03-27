from django.urls import path
from . import views

app_name = 'sales_app'

urlpatterns = [
    # Home page
    path('', views.sales_homepage, name='sales_homepage'),
    path('new_sale/', views.add_sale, name='add_sale'),
    path('new_product/', views.add_product, name='add_product'),
    path('view_sales/', views.see_sales, name='see_sales'),
    path('sale/<int:sale_id>', views.see_sale, name='see_sale'),
    path('view_products/', views.see_products, name='see_products'),
    path('product/<int:product_id>', views.see_product, name='see_product'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('dealerjobs/', views.see_dealer_jobs, name='see_dealer_jobs'),
    path('dealerjob/<int:job_id>', views.see_dealer_job, name='see_dealer_job'),
]