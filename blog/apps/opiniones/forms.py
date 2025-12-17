from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinion
        fields = ["texto"]
        error_messages = {
            'texto': {
                'required': '',
            }
        }
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu opinión aquí...'
            })
        }