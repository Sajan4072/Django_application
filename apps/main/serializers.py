from rest_framework import serializers


from .models import Inputs 

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inputs
        fields=['time','distance']
    
    def validate_distance(self,value):
        if value<=0:
            raise serializers.ValidationError("Distance cannot be negative")
        return value 
    
    
