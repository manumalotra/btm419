from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sale, DealerJob

@receiver(post_save, sender=Sale)
def create_dealer_job(sender, instance, created, **kwargs):
    print('hello')
    if created and instance.product.product_type == 1:
        DealerJob.objects.create(sale=instance)

# This is Jaiden to Robb - over