#claims_app/forms.py
from django import forms
from .models import Claim

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ('claim_type', 'claim_desc', 'claim_photo', 'sale_id')
        labels = {'text':'Enter Claim:'}
        
