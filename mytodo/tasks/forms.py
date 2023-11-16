from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from .models import *
class TaskForm(forms.ModelForm):
	class Meta:
		model=Task
		fields='__all__'

	widgets = {
            'title': TextInput(attrs={
     
                'placeholder': 'Name'
                }),
            'points': NumberInput(attrs={
                'class': "form-control2", 
                'style': 'width: 5px;',
                'placeholder': 'Email'
                })
        }	