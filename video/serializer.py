from rest_framework import serializers
from .models import video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = [
            "id",
            "title",
            "video_size",
            "video_description",
            "video_file",
            "genre",
            "release_date",
            "language",
            "age_rating",
            "cast",
            "directors",
            "produced_at",
            "thumbnail",
            "video_duration",
        ]