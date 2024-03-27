from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SaleForm
from .models import Sale

# Create your views here.
# Create your views here.
def sales_homepage(request):
    """The home page for Sales App."""
    return render(request, 'sales_app/sales_homepage.html')

@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            # Process the form data and save the new sale
            sale = Sale(
                sale_amount=form.cleaned_data['sale_amount'],
                product_name=form.cleaned_data['product_name'],
                digital_signature=form.cleaned_data['digital_signature'],
                # Assign other form fields to Sale model fields
            )
            sale.save()
            # Redirect to a success page or main page
            return redirect('sales_app:sales_homepage')
    else:
        form = SaleForm()

    return render(request, 'sales_app/add_sale.html', {'form': form})