from django import forms
from .models import Partymenu


class PartymenuForm(forms.ModelForm):
    class Meta:
        model = Partymenu
        fields = '__all__'

        