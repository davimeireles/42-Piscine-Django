from django import forms
from .models import Movies

class RemoveMovieForm(forms.Form):
    title = forms.ModelChoiceField(
        queryset=Movies.objects.all(),
        to_field_name='title',
        label='Select a Movie to remove'
    )
