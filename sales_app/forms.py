# sales_app/forms.py
from django import forms
from .models import Sale, Product, DealerJob

class ProductForm(forms.ModelForm):
    CHOICES1 = (
            (1, 'Regular Product'),
            (2, 'Extended Warranty'),
        )
        
    product_type = forms.ChoiceField(choices=CHOICES1, label='Product type')

    class Meta:
        model = Product
        fields = ('product_name', 'product_type', 'product_price', 'product_desc', 'product_photo')
        exclude = ['product_id', 'employee']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_photo'].required = False
        
class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ('product', 'digital_signature')
        exclude = ['sale_id', 'customer', 'sale_date']

class DealerJobForm(forms.ModelForm):
    CHOICES2 = (
            (2, 'Product Applied'),
            (3, 'Unable to Apply Product'),
        )
        
    job_status = forms.ChoiceField(choices=CHOICES2, label='Indicate Status of Job')

    class Meta:
        model = DealerJob
        fields = ('job_status', 'job_desc', 'job_photo')
        exclude = ['job_id', 'job_date', 'sale', 'job_staff']

    def __init__(self, *args, **kwargs):
        super(DealerJobForm, self).__init__(*args, **kwargs)
        self.fields['job_photo'].required = False