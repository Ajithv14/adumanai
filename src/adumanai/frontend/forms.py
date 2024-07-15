from django import forms

class FormCake(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    url = forms.CharField()
