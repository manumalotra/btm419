from django.urls import path
from . import views

app_name = 'claims_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('get_claims/',views.get_claims, name='get_claims'),
    path('get_claims/<int:claim_id>', views.get_claims, name='get_claims'),
]