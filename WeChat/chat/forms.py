from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ChatForm(forms.ModelForm):
	class Meta:
		model = ChatModel
		fields = ['text']
		widgets = {
			'text': forms.Textarea(attrs={'class': 'form-control', 'style':'resize: none;', 'rows': 2}),
		}


class MailForm(forms.Form):
	mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style':'margin-left: 10px; margin-right: 10px'}))
	subject = forms.CharField(label='Тема', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style':'margin-left: 10px; margin-right: 10px'}))
	text = forms.CharField(label='Текст', max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control', 'style':'resize: none; margin-left: 10px; margin-right: 10px;', 'rows': 4}))
