from django import forms
from .models import People

class Ex10form(forms.Form):
    mov_min_release_date = forms.DateField(
        label='Movies minimum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    mov_max_release_date = forms.DateField(
        label='Movies maximum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    plan_diameter_grater_than = forms.FloatField(
        label='Planet Diameter'
    )
    character_gender = forms.ChoiceField(
        label='Character Gender',
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_genders = People.objects.values_list('gender', flat=True).distinct()
        self.fields['character_gender'].choices = [(gender, gender) for gender in unique_genders if gender]