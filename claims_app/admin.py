from django.contrib import admin

# Register your models here.
from .models import Claim, ClaimRepair

admin.site.register(Claim)
admin.site.register(ClaimRepair)