from django.contrib import admin

# Register your models here.
from .models import CostResultsInfo, CostResultsCell, CostResultsKwh

admin.site.register(CostResultsInfo)
admin.site.register(CostResultsCell)
admin.site.register(CostResultsKwh)