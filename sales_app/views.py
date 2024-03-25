from django.shortcuts import render

# Create your views here.
# Create your views here.
def sales_homepage(request):
    """The home page for Sales App."""
    return render(request, 'sales_app/sales_homepage.html')