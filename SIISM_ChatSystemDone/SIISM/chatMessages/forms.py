
from django import forms
from django.forms import ModelForm
#from django.forms import BaseForm

from .models import Message

class NewMessageForm(forms.ModelForm):
	class Meta:
		model = Message
	
		fields = ['text']