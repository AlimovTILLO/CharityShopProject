from django.contrib import admin
from item.models import Item, Comments


# Register your models here.
class ItemInline(admin.StackedInline):
    model = Comments
    extra = 2

class ItemAdmin(admin.ModelAdmin):
    fields = ['item_title', 'item_text', 'item_image', 'item_date']
    inlines = [ItemInline]
    list_filter = ['item_date']

admin.site.register(Item, ItemAdmin)
