from django import forms

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del autor:')
    apellidos = forms.CharField(max_length=200, label="Apellidos del autor:")
    fecha_nac = forms.DateField(label='Fecha de nacimiento del autor:')

