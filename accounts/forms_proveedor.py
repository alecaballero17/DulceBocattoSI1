from django import forms
from .models_db import Proveedor   # o desde donde tengas tu modelo real


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "tipo", "telefono", "direccion"]
