from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    """The home page for Sales App."""
    return render(request, 'sales_app/index.html')