from django import forms

class Add_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan URL',
    }
    name_attrs = {
        'type':'text',
    	'class':'form-control',
        'placeholder': 'Azmie'
    }
    url_attrs = {
        'type':'url',
    	'class':'form-control',
        'placeholder': 'https://google.com'
    }

    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs=name_attrs))
    url = forms.URLField(label='URL', required=True, widget=forms.TextInput(attrs=url_attrs))
