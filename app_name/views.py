from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app_name.serializers import UploadSerializer

# Create your views here.

# Lets create the viewsets

class UploadViewSet(ViewSet):
    #1. properties
    # Creating the object from a Class()
    # objectName = ClassName();
    serializer_class_object = UploadSerializer()
    
    #2. Constructor
    
    #3 Method
    def list(self, request):
        # every method return something
        return Response('OK GoodMorning')
        
    def create(self,request):
        file_uploaded = request.FILES.get('file_uploaded');
        print(file_uploaded)
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
    
    #4. Nested Class
    pass
