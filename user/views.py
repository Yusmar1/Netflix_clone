from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserListCreateView(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                CustomUserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class GetSingleUser(APIView):
    def get(self, request, param):
        user = get_object_or_404(CustomUser, id=param)

        serialize_user = CustomUserSerializer(user)
        return Response({"message": "user details gotten successfully", "data": serialize_user.data}, status.HTTP_200_OK)