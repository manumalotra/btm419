from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Claim, ClaimRepair
from sales_app.models import Sale
from .forms import ClaimForm, ClaimReviewForm, ClaimRepairForm
from datetime import date


# Create your views here.
def index(request):
    """The home page for Claims."""
    return render(request, 'claims_app/index.html')

@login_required
def get_claims(request):
    """Find all claims"""
    claimslistcust = Claim.objects.filter(sale_id__customer=request.user).order_by('claim_id')
    claimslist = Claim.objects.order_by('claim_id')
    context={'Claims':claimslist, 'CustClaims':claimslistcust}

    return render(request, 'claims_app/get_claims.html', context)

@login_required
def get_claim(request, claim_id):
    """Show a single claim and its contents."""
    myclaim = Claim.objects.get(pk=claim_id)
    if request.method == 'POST':
        form = ClaimReviewForm(request.POST, request.FILES, instance=myclaim)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.claim_id = claim_id
            instance.decision_date = date.today()
            instance.deciding_staff = request.user
            instance.save()
            return redirect('claims_app:get_claims')
        else:
            print(form.errors)  
    else:
        form = ClaimReviewForm()
    context = {'Claim': myclaim, 'form': form}
    return render(request, 'claims_app/get_claim.html', context)

@login_required
def new_claim(request, sale_id):
    """Add a new claim."""
    mysale = Sale.objects.get(pk=sale_id)
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.claim_type = mysale.product.product_type
            instance.claim_date = date.today()
            instance.claim_status = 0
            instance.sale_id = mysale
            instance.save() 
            return redirect('claims_app:index') 
        else:
            print(form.errors) 
    else:
        form = ClaimForm()
    return render(request, 'claims_app/new_claim.html', {'form': form})

@login_required
def get_claim_repairs(request):
    repairslistcust = ClaimRepair.objects.filter(claim_id__sale_id__customer=request.user).order_by('claim_id')
    repairslist = ClaimRepair.objects.order_by('repair_id')
    context={'ClaimRepairs':repairslist, 'CustRepairs':repairslistcust}

    return render(request, 'claims_app/get_claim_repairs.html', context)

# Hi Robb

@login_required
def get_claim_repair(request, repair_id):
    myrepair = ClaimRepair.objects.get(pk=repair_id)
    if request.method == 'POST':
        form = ClaimRepairForm(request.POST, request.FILES, instance=myrepair)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.repair_id = repair_id
            instance.repair_date = date.today()
            instance.repair_staff = request.user
            instance.save()
            return redirect('claims_app:get_claim_repairs')
        else:
            print(form.errors) 
    else:
        form = ClaimRepairForm()
    context = {'ClaimRepair': myrepair, 'form': form}
    return render(request, 'claims_app/get_claim_repair.html', context)