from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите теги через запятую'}), required=False)
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']