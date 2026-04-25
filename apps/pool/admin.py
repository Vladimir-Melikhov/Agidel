from django.contrib import admin
from .models import Actions, Lead, Certificate


@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    list_filter = ("is_active",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", 
                    "phone_number",
                    "messenger",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "img",
        "title"
    )
