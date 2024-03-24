#claims_app/forms.py
from django import forms
from .models import Claim

class ClaimForm(forms.ModelForm):
    CHOICES1 = (
            (1, 'Product Warranty Claim'),
            (2, 'Extended Warranty Claim'),
            # Add more choices as needed
        )
        
    claim_type = forms.ChoiceField(choices=CHOICES1, label='claim_type')

    class Meta:
        model = Claim
        fields = ('claim_type', 'claim_desc', 'claim_photo', 'sale_id')
        exclude = ['claim_id', 'claim_date', 'claim_status', 'repair_status']
        
