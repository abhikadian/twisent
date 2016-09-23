from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Item', max_length=140)