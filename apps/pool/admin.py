from django.contrib import admin
from .models import Actions, Lead, Certificate, Service, Trainer


@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    list_filter = ("is_active",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", 
                    "phone_number",
                    "messenger",
                    "consent_personal_data",
                    "consent_terms",
                    "created_at",)
    readonly_fields = ("consent_at", "created_at")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "img",
        "title"
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "haveprice",
        "is_active",
        "order_id",
        "price"
    )


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "experience", "order", "is_active")
    list_editable = ("order", "is_active")
