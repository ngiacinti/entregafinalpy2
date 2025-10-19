from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Contenido', 'rows': 6, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

class SearchForm(forms.Form):
    q = forms.CharField(
        label='Buscar por título',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por título', 'class': 'form-control'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
