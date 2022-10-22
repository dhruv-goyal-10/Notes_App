from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from base.models import *
from .serializers import *


@api_view(['GET'])
def allNotes(request):
        Note = Addnote.objects.all()

        serializer = AddnoteSerializer(Note, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def searchNotes(request,pk):
        Note = Addnote.objects.all()
        search_input = pk 
        if search_input:
            Note = Addnote.objects.filter(noteTitle__startswith=search_input)
        serializer = AddnoteSerializer(Note, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def viewNote(request,pk):
    Note = Addnote.objects.get(id=pk)
    serializer = AddnoteSerializer(instance=Note, many= False)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def createNotes(request):
   serializer = AddnoteSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
   return JsonResponse(serializer.data)

@api_view(['GET','PUT'])
def updateNotes(request, pk):
    Note = Addnote.objects.get(id=pk)
    serializer = AddnoteSerializer(instance=Note,data=request.data)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def deleteNotes(request, pk):
    Note = Addnote.objects.get(id=pk)
    Note.delete()
    return HttpResponse("Deleted Successfully")