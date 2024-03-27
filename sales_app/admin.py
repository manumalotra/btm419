from django.contrib import admin
from .models import Sale, Product, DealerJob

# Register your models here.

admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(DealerJob)