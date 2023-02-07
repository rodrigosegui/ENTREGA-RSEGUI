from django import forms

# Create your forms here.
class HuespedFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()


class AlojamientosFormulario(forms.Form):

    nombreA = forms.CharField(max_length=20)
    capacidad = forms.IntegerField()
    habitaciones = forms.IntegerField()
    precioxdia = forms.FloatField()


class VehiculosFormulario(forms.Form):

    nombreV = forms.CharField(max_length=40)
    asientos = forms.IntegerField()
    preciodiario = forms.FloatField()