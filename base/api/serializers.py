from dataclasses import field
from rest_framework.serializers import ModelSerializer
from base.models import *

class AddnoteSerializer(ModelSerializer):
    class Meta:
        model = Addnote
        fields = '__all__'
