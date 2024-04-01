from django.shortcuts import render
from sales_app.models import Product

# Create your views here.

def index(request):
    """The main home page for the whole C3 website."""
    products = Product.objects.all()
    return render(request, 'main_homepage_app/index.html', {'Products': products})