from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display

from .models import Actions, Lead, Certificate, Service, Trainer


@admin.register(Actions)
class ActionsAdmin(ModelAdmin):
    list_display = ("title", "description", "image")
    list_filter = ("is_active",)


@admin.register(Lead)
class LeadAdmin(ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "messenger",
        "consent_personal_data",
        "consent_terms",
        "created_at",
    )
    search_fields = ("name", "phone_number")
    readonly_fields = ("consent_at", "created_at")


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ("img", "title")


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "haveprice",
        "is_active",
        "order_id",
        "price",
    )


@admin.register(Trainer)
class TrainerAdmin(ModelAdmin):
    list_display = ("photo_preview", "last_name", "first_name", "experience", "order", "is_active")
    list_display_links = ("last_name", "first_name")
    list_editable = ("order", "is_active")

    @display(description="Фото")
    def photo_preview(self, obj):
        if not obj.photo:
            return "—"
        return format_html(
            '<img src="{}" style="width:44px;height:44px;object-fit:cover;border-radius:12px;">',
            obj.photo.url,
        )
