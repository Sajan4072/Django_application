from django import forms
from django.db.models import fields

from .models import Inputs

# MAX_TWEET_LENGTH=300

class InputForm(forms.ModelForm):
    class Meta:
        model=Inputs
        fields=['time','distance']
        
        widgets={
            'time':forms.TimeInput(attrs={'class':'form-control form-control-lg','id':'time','placeholder':'Time(hh:mm)'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-lg','id':'distance','placeholder':'Distance(Km)'}),
            
        }


    def clean_distance(self):
        distance=self.cleaned_data.get('distance')
        if distance<=0:
            raise forms.ValidationError("Distance cannot be negative")
        return distance


    def clean_time(self):
        time=self.cleaned_data.get('time')
        if time<0:
            raise forms.ValidationError("Time cannot be negative")
        return time