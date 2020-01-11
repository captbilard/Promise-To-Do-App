from django import forms
from django.forms import TextInput

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {'task': TextInput(attrs={'class':'form-control','placeholder':'Add Todo'})}