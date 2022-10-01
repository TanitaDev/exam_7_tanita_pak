from django import forms


class EntryForm(forms.Form):
    name = forms.CharField(max_length=200, label="Имя", widget=forms.TextInput(attrs={'class': 'name_input'}))
    mail = forms.EmailField(max_length=254, label="Почта", widget=forms.TextInput(attrs={'class': 'mail_input'}))
    text = forms.CharField(max_length=3000, label="Текст записи", widget=forms.TextInput(attrs={'class': 'text_input'}))
