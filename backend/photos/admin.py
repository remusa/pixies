import arrow

from django.contrib import admin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    model = Photo

    list_display = (
        "caption",
        "details",
        "created",
        "updated",
        "url",
    )

    def created(self, obj):
        return arrow.get(obj.created_at).humanize()

    def updated(self, obj):
        return arrow.get(obj.updated_at).humanize()
