from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SaleForm, ProductForm, DealerJobForm
from .models import Sale, Product, DealerJob
from datetime import date

# Create your views here.
# Create your views here.
def sales_homepage(request):
    """The home page for Sales App."""
    return render(request, 'sales_app/sales_homepage.html')

@login_required
def thankyou(request):
    user = request.user
    return render(request, 'sales_app/thank_you.html', {'User':user})

@login_required
def see_sales(request):
    saleslistcust = Sale.objects.filter(customer=request.user).order_by('sale_id')
    saleslist = Sale.objects.order_by('sale_id')
    context={'Sales':saleslistcust, 'AllSales': saleslist}

    return render(request, 'sales_app/view_sales.html', context)

@login_required
def see_sale(request, sale_id):
    """Show a single sale and its contents."""
    mysale = Sale.objects.get(pk=sale_id)
    context = {'Sale': mysale}
    return render(request, 'sales_app/view_sale.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.employee = request.user
            instance.save()
            return redirect('sales_app:see_products')
        else:
            print(form.errors)  
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'sales_app/add_product.html', context)

@login_required
def see_products(request):
    productlist = Product.objects.order_by('product_id')
    context={'Products':productlist}

    return render(request, 'sales_app/view_products.html', context)

@login_required
def see_product(request, product_id):
    myproduct = Product.objects.get(pk=product_id)
    context = {'Product': myproduct}
    return render(request, 'sales_app/view_product.html', context)

@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = request.user
            instance.sale_date = date.today()
            instance.save()
            return redirect('sales_app:thankyou')
        else:
            print(form.errors)  
    else:
        form = SaleForm()
    context = {'form': form}
    return render(request, 'sales_app/add_sale.html', context)

@login_required
def see_dealer_jobs(request):
    custjobslist = DealerJob.objects.filter(sale__customer=request.user).order_by('job_id')
    jobslist = DealerJob.objects.order_by('job_id')
    context={'Jobs':jobslist, 'CustJobs':custjobslist}

    return render(request, 'sales_app/view_jobs.html', context)

# Hi Robb

@login_required
def see_dealer_job(request, job_id):
    myjob = DealerJob.objects.get(pk=job_id)
    if request.method == 'POST':
        form = DealerJobForm(request.POST, request.FILES, instance=myjob)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.job_id = job_id
            instance.job_date = date.today()
            instance.job_staff = request.user
            instance.save()
            return redirect('sales_app:see_dealer_jobs')
        else:
            print(form.errors) 
    else:
        form = DealerJobForm()
    context = {'Job': myjob, 'form': form}
    return render(request, 'sales_app/view_job.html', context)