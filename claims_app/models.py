from django.db import models
from sales_app.models import Sale

# Create your models here.
class Claim(models.Model):
    claim_id = models.IntegerField()
    claim_type = models.IntegerField()
    claim_desc = models.CharField(max_length = 200)
    claim_date = models.DateField()
    claim_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    repair_status = models.IntegerField()
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Sale ID: {self.sale_id}, Claim Date: {self.claim_date}"
