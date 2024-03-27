from django.shortcuts import render

# Create your views here.

def reports_home(request):
    # Add any necessary logic here
    return render(request, 'reports_app/reports_home.html')
