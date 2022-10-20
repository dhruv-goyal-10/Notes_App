from django.shortcuts import redirect, render, HttpResponse
from base.models import Addnote

# Create your views here.

def home(request):
    if request.method=="POST":
        title=request.POST['title']
        desc =request.POST['description']
        obj= Addnote(noteTitle = title, noteDesc=desc)
        obj.save()
    return(render(request,'home.html'))


def list(request):
    allNotes=Addnote.objects.all()
    print(allNotes)
    list={'list': allNotes}
    return(render(request,'list.html', list))

 
def delete_note(request, id):
    temp=Addnote.objects.get(pk =id)
    temp.delete()
    return redirect('list')
     
     
 