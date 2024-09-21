from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .tasks import my_task
# Create your views here.


class MyView(APIView):
    def get(self, request):
        print("here")
        my_task.delay()
        return Response("Success", status=status.HTTP_200_OK)
