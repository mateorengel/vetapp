from django import forms
from .models import Pet, Veterinarian

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

class VeterinarianForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = '__all__'