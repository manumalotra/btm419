from django.db import models
from sales_app.models import Sale

# Create your models here.
class Claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    claim_type = models.IntegerField() # 1 for: Product Warranty Claim, 2 for: Extended Warranty Claim
    claim_desc = models.CharField(max_length = 200)
    claim_date = models.DateField()
    claim_photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    claim_status = models.IntegerField(default=0) # 0 for: Under Review, 1 for: Denied, 2 for: Accepted
    repair_status = models.IntegerField() # 0 for: N/A, 1 for: Ready for Repair, 2 for: Repaired
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Sale ID: {self.sale_id}, Claim Date: {self.claim_date}"
