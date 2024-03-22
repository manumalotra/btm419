from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Claim
from .forms import ClaimForm


# Create your views here.
def index(request):
    """The home page for Claims."""
    return render(request, 'claims_app/index.html')

def get_claims(request):
    """Find all claims"""
    claimslist = Claim.objects.order_by('claim_date')
    context={'Claims':claimslist}

    return render(request, 'claims_app/get_claims.html', context)

def get_claim(request, claim_id):
    """Show a single claim and its contents."""
    myclaim = Claim.objects.get(id=claim_id)
    context = {'Claim': myclaim}
    return render(request, 'claims_app/get_claim.html', context)

def new_claim(request):
    """Add a new claim."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClaimForm()
    else:
        # POST data submitted; process data.
        form = ClaimForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('claims_app:claims')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'claims_app/new_claim.html', context)
