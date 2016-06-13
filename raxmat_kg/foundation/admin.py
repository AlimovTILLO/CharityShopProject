from django.contrib import admin

from models import Foundation, FoundationCategory


class FoundationCategoryAdmin(admin.ModelAdmin):
    fields = ['foundation_category_name']


class FoundationAdmin(admin.ModelAdmin):
    fields = ['foundation_category', 'foundation_name', 'foundation_description', 'foundation_logo', 'foundation_status', 'foundation_url']


admin.site.register(FoundationCategory, FoundationCategoryAdmin)
admin.site.register(Foundation, FoundationAdmin)
