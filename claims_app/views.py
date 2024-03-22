from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Claim

# Create your views here.
def index(request):
    """The home page for Claims."""
    return render(request, 'claims_app/index.html')

def get_claims(request):
    """Find all claims"""
    claimslist = Claim.objects.order_by('claim_date')
    context={'Claims':claimslist}

    return render(request, 'claims_app/get_claims.html')

def claim(request, claim_id):
    """Show a single claim and its contents."""
    myclaim = Claim.objects.get(id=claim_id)
    myentries = myclaim.entry_set.order_by('-date_added')
    context = {'Claim': myclaim}
    return render(request, 'claims/get_claim.html', context)

