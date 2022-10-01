from django import forms


class EntryForm(forms.Form):
    name = forms.CharField(max_length=200)
    mail = forms.EmailField(max_length=254)
    text = forms.CharField(max_length=3000)
