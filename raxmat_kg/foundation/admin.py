from django.contrib import admin

from foundation.models import Foundation


# Register your models here.
class FoundationAdmin(admin.ModelAdmin):
    fields = ['foundation_name', 'foundation_description', 'foundation_logo']


admin.site.register(Foundation, FoundationAdmin)
