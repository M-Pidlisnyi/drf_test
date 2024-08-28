from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "message", "email")

    def name(self, obj):
        return obj.title
    def message(self, obj):
        return obj.description

# admin.site.register(Contact)