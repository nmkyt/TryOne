from django import forms
from .models import TypingText


class TextForm(forms.ModelForm):
    class Meta:
        model = TypingText
        fields = ['content']
