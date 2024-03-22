from django.shortcuts import render

# Create your views here.

def index(request):
    """The main home page for the whole C3 website."""
    return render(request, 'main_homepage_app/index.html')