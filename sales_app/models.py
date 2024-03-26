from django.db import models

# Create your models here.

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_amount = models.DecimalField(max_digits=10, decimal_places = 2)
    product_name = models.CharField(max_length=200)
    digital_signature = models.CharField(max_length=200)

    def __str__(self):
        return f"Sale ID: {self.sale_id}, Sale Amount: {self.sale_amount}, Digital Signature: {self.digital_signature}"

class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    customer_email = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name

