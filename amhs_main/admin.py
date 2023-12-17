from .models import Contact
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


admin.site.register(Contact, ContactAdmin)
