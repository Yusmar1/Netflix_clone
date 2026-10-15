from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "user",
            "plan",
            "price",
            "status",
            "start_date",
            "end_date",
            "payment_id",
            "payment_status",
            "auto_renewal",
            "time_created",
            "date_created",
        ]