from django.contrib import admin
from .models import BloodInventoryModel,BloodRequestModel,DonorModel
# Register your models here.
admin.site.register(DonorModel)
admin.site.register(BloodInventoryModel)
admin.site.register(BloodRequestModel)