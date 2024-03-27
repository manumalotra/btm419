#claims_app/forms.py
from django import forms
from .models import Claim, ClaimRepair

class ClaimForm(forms.ModelForm):
    CHOICES1 = (
            (1, 'Product Warranty Claim'),
            (2, 'Extended Warranty Claim'),
        )
        
    claim_type = forms.ChoiceField(choices=CHOICES1, label='Claim type')

    class Meta:
        model = Claim
        fields = ('claim_type', 'claim_desc', 'claim_photo')
        exclude = ['claim_id', 'claim_date', 'claim_status', 'deciding_staff', 'sale_id']
        
class ClaimReviewForm(forms.ModelForm):
    CHOICES1 = (
            (1, 'Deny Claim'),
            (2, 'Approve Claim'),
        )
        
    claim_status = forms.ChoiceField(choices=CHOICES1, label='Approve claim?')

    class Meta:
        model = Claim
        fields = ('claim_status',)
        exclude = ['claim_id', 'claim_type', 'claim_date', 'claim_desc', 'claim_photo', 'sale_id', 'deciding_staff']

class ClaimRepairForm(forms.ModelForm):
    CHOICES2 = (
            (2, 'Repaired'),
            (3, 'Unable to Repair'),
        )
        
    repair_status = forms.ChoiceField(choices=CHOICES2, label='Indicate Status of Repair')

    class Meta:
        model = ClaimRepair
        fields = ('repair_status', 'repair_desc', 'repair_photo')
        exclude = ['repair_id', 'repair_date', 'claim_id', 'repair_staff']

    def __init__(self, *args, **kwargs):
        super(ClaimRepairForm, self).__init__(*args, **kwargs)
        self.fields['repair_photo'].required = False

# Jaiden waz here