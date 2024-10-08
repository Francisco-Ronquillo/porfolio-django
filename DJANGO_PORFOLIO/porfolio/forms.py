from django import forms
from .models import Referencias_laborales

class Referencias(forms.ModelForm):
    class Meta:
        model=Referencias_laborales
        fields=['nombre_test','relacion','telefono','correo','descripcion']
