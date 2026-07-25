from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "subject",
        "short_message",
        "created_at",
    )

    search_fields = (
        "user__username",
        "subject",
        "message",
    )

    list_filter = (
        "created_at",
    )

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    short_message.short_description = "Message"