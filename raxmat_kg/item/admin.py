from django.contrib import admin
from item.models import MainCategory, ItemCategory, Item, Comments


# Register your models here.
class MainCategoryAdmin(admin.ModelAdmin):
    fields = ['main_category_name']


class ItemCategoryAdmin(admin.ModelAdmin):
    fields = ['item_category_main_id', 'item_category_name']


class ItemInline(admin.StackedInline):
    model = Comments
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    fields = ['item_title', 'item_description', 'item_date', 'item_image', 'item_price', 'item_charity',
              'item_category_id']

    inlines = [ItemInline]
    list_filter = ['item_date']


admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)