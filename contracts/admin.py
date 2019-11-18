from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'user', 'manager', 'start_date', 'end_date', 'if_signed')
    list_display_links = ('id', 'listing')
    search_fields = ('listing', 'user', 'manager', 'start_date', 'end_date')
    list_per_page = 25


admin.site.register(Contract, ContractAdmin)
