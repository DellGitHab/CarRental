from django import forms
from CarRent.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'