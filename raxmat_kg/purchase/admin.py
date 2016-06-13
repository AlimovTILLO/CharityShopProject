from django.contrib import admin

from purchase.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    fields = ['purchase_user', 'purchase_item', 'purchase_sales_date', 'purchase_pin']


admin.site.register(Purchase, PurchaseAdmin)
