from django import forms
from ..models import Professor

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'senha']
    

      