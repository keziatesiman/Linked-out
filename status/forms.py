from django import forms

class Update_Bar(forms.Form):
    error_messages = {
        'required': 'Isi duls',
    }
    update_attrs = {
        'type': 'text',
        'cols': 150,
        'rows': 4,
        'class': 'update-textarea',
        'placeholder': 'sup?'
    }
    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=update_attrs))
