from django import forms
from incidenciasApp.models import Incidencia

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'comentario': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese su comentario aquí'}),
        }