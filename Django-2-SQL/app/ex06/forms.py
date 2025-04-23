from django import forms

class UpdateRowForm(forms.Form):
    opening_craw = forms.ChoiceField(label='Opening Craw')