from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Claim, ClaimRepair

@receiver(post_save, sender=Claim)
def create_claim_repair(sender, instance, created, **kwargs):
    if instance.claim_status == 2:  # Status is approved
        ClaimRepair.objects.create(claim_id=instance)