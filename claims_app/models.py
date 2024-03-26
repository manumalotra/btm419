from django.db import models
from sales_app.models import Sale

# Create your models here.
class Claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    claim_type = models.IntegerField() # 1 for: Product Warranty Claim, 2 for: Extended Warranty Claim
    claim_desc = models.CharField(max_length = 200)
    claim_date = models.DateField()
    decision_date = models.DateField(null=True)
    claim_photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    claim_status = models.IntegerField(default=0) # 0 for: Under Review, 1 for: Denied, 2 for: Accepted
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Claim Date: {self.claim_date}"
    
class ClaimRepair(models.Model):
    repair_id = models.AutoField(primary_key=True)
    repair_desc = models.CharField(max_length = 200, null=True)
    repair_date = models.DateField(null=True)
    repair_photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)
    repair_status = models.IntegerField(default=1) # 1 for: Ready for Repair, 2 for: Repaired
    claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)

    def __str__(self):
        return f"Repair ID: {self.repair_id}"