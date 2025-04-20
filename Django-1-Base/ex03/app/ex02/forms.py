from django import forms

class PersonForm(forms.Form):
    input_name = forms.CharField(label='Name', max_length=15)
    input_last_name = forms.CharField(label='Last Name', max_length=15)
    input_age = forms.IntegerField(label='Age', min_value=1, max_value=100)