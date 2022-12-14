from email.policy import default
from django.db import models

class Addnote(models.Model):
    noteTitle = models.CharField(max_length=30)
    noteDesc = models.TextField(max_length=200)
    time= models.DateTimeField(auto_now_add= True) 
    bookmark = models.IntegerField(default=0)

    def __str__(self): 
        return self.noteTitle