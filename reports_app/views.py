from django.shortcuts import render
from sales_app.models import Sale
from claims_app.models import Claim

# Create your views here.

def reports_home(request):
    # Add any necessary logic here
    return render(request, 'reports_app/reports_home.html')

def sales_report(request):
    # Fetch sales data from the database
    sales_data = Sale.objects.all()  # Example: Fetch all sales data
    
    # Pass the data to the template for rendering
    return render(request, 'reports_app/sales_report.html', {'sales_data': sales_data})

def claims_report(request):
    claims = Claim.objects.all()
    return render(request, 'reports_app/claims_report.html', {'claims': claims})