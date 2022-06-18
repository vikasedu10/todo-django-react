from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Note
from api.serializers import NoteSerializer

@api_view(['GET'])
def home(request):
    return Response('Our API')

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)
    
