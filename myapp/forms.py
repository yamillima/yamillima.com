from django import forms
from django.forms import TextInput
from .models import Lead


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ('name', 'email', 'whatsapp_number', 'department', 'city')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': TextInput(attrs={'placeholder': 'Correo electrónico'}),
            'whatsapp_number': TextInput(attrs={'placeholder': 'Número de WhatsApp'}),
            'department': TextInput(attrs={'placeholder': 'Departamento'}),
            'city': TextInput(attrs={'placeholder': 'Ciudad o municipio'}),
        }
