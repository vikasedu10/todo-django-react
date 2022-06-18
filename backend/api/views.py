from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Note
from api.serializers import NoteSerializer


@api_view(['GET', 'POST', 'DELETE'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    try:
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return Response(serializer.data)
    except Note.DoesNotExists:
        return JsonResponse({'message': 'This note does not exists'}, status=status.HTTP_404_NOT_FOUND)
    
