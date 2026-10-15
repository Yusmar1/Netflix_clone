from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import video
from .serializer import VideoSerializer

class VideoListCreateViews(APIView):

    def get(self, request):
        view = video.objects.all()
        serializers = VideoSerializer(view, many = True)

        return Response(serializers.data)
