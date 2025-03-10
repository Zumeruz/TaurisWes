from django import forms
from blog.models import *



class PostForms(forms.ModelForm):
    class Meta:
        model=Forma
        fields='__all__'