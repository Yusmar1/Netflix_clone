from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionListCreateViews(APIView):

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializers = SubscriptionSerializer(subscriptions, many = True)

        return Response(serializers.data)

