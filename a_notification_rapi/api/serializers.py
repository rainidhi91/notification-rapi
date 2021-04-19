from rest_framework import serializers
from a_notification_rapi.models import Notification
from django.utils.timesince import timesince


class NotificationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at", "created_by", "sent_date_time",)

    def get_created_at(self, instance):
        return timesince(instance.created_at)

    def get_updated_at(self, instance):
        return timesince(instance.updated_at)