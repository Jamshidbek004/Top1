from django import forms
from .models import Mijoz,Oquvchilar

class MijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields =['ismi', 'raqami']
class mijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields =['etabi']

class OquvchiForm(forms.ModelForm):
    class Meta:
        model = Oquvchilar
        fields ='__all__'