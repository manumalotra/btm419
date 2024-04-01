from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_type = models.IntegerField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_desc = models.CharField(max_length=200, null=True)
    product_photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.product_id}: {self.product_name} - ${self.product_price}"

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_date = models.DateField(default=date.today())
    digital_signature = models.CharField(max_length=20)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sale #{self.sale_id} - Product: {self.product.product_name} @ ${self.product.product_price}. Purchased by {self.customer}"
    
class DealerJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_desc = models.CharField(max_length = 200, null=True)
    job_date = models.DateField(null=True)
    job_photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)
    job_status = models.IntegerField(default=1) # 1 for: Ready for Application, 2 for: Applied
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    job_staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Job ID: {self.job_id}"