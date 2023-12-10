from django import forms
from vehiculosApp.models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
            'ano_fabricacion': forms.DateInput(attrs={'type': 'date'}),
        }