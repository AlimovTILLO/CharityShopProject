from django.contrib import admin

from purchase.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    fields = ['user', 'item', 'sales_date', 'pin']


admin.site.register(Purchase, PurchaseAdmin)
