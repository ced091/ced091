# forms.py
from django import forms
from .models import Commentaire

class StarRatingWidget(forms.Widget):
    template_name = 'libeiki/stars.html'

    def format_value(self, value):
        return str(value)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['pseudo', 'note', 'texte']