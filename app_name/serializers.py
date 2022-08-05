from django.forms import FileField
from rest_framework.serializers import Serializer

# let create a file

class UploadSerializer(Serializer):
    #1. properties
    file_uploaded = FileField()
    
    #2. Constructor
    
    #3 Method
    
    #4. Nested Class
    class Meta():
        
        #1. properties
        fields = ['file_uploaded']
    
        #2. Constructor
        
        #3 Method
        
        #4. Nested Class
        pass
    pass