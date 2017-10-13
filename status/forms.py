from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    status_attrs = {
        'type': 'text',
        'cols': 150,
        'rows': 4,
        'class': 'status-form-textarea',
        'placeholder':'Apa yang sedang kamu pikirkan?'
    }

    status = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=status_attrs))
