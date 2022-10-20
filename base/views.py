from django.shortcuts import render, HttpResponse
from base.models import Note

# Create your views here.

def home(request):
    if request.method=="POST":
        title=request.POST['title']
        desc =request.POST['description']
        obj= Note(noteTitle = title, noteDesc=desc)
        obj.save()
    return(render(request,'home.html'))


def list(request):
    allNotes=Note.objects.all()
    print(allNotes)
    list={'list': allNotes}
    return(render(request,'list.html', list))
 