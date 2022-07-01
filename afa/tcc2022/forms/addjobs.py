from django import forms
from ..models import SubArea

class AddJobs(forms.Form):
    area = forms.CharField(max_length = 50,required = True)
    subarea = forms.CharField(max_length = 50,required = True)
    trabdaArea = forms.CharField(max_length = 250,required = True)
    textAreacss = forms.TextInput()

