from django import forms


class SearchTagForm(forms.Form):
    search = forms.CharField(max_length=100)
