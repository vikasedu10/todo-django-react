from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response('Our API')

@api_view(['GET'])
def getNotes(request):
    return Response("Notes")
    
