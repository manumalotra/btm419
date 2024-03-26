# sales_app/forms.py
from django import forms

class SaleForm(forms.Form):
    # sale_id = forms.DecimalField(label='Sale ID (Automatically generated)')
    sale_amount = forms.DecimalField(label='Sale Amount')
    product_name = forms.CharField(label='Product Name')
    digital_signature = forms.CharField(label="Digital Signature")
    # Add more fields as needed
