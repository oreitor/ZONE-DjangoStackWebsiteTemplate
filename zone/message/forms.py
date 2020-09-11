from django import forms
from .models import Message

class Form(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'text')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Write your name here...'}),
            'email': forms.EmailInput(attrs={
                'class':'form-control', 'placeholder': 'Write your email here...'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control', 'rows': '5', 'placeholder': 'Write your text here...'})
        }