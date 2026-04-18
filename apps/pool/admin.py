from django.contrib import admin
from .models import Actions


@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    list_filter = ("is_active",)
