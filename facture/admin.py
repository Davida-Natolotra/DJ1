from django.contrib import admin
from .models import FactureOperation, FactureMoto, BLMoto
# Register your models here.
admin.site.register(FactureOperation)
admin.site.register(FactureMoto)
admin.site.register(BLMoto)
