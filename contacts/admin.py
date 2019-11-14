from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date', 'manager_id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing', 'manager_id')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
