from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ("image","name","price")


admin.site.register(Item, ItemAdmin)
