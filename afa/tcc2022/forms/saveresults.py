from django import forms
from ..models import EscolhaProf

class SaveNotasModelForm(forms.ModelForm):
    class Meta:
        model = EscolhaProf
        fields = ['nota']