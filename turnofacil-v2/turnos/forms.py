from django import forms
from .models import Turno


class TurnoForm(forms.ModelForm):

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Turno
        fields = [
            'cliente',
            'fecha',
            'hora',
            'descripcion',
            'profesional'
        ]