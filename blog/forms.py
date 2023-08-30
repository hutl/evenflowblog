from django import forms
from .models import Comentario

class AddComentario (forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome','texto',)