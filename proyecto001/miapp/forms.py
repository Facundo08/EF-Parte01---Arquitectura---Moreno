from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
