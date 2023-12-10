from django import forms
from mantencionApp.models import Mantenimiento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date',}), 

        }