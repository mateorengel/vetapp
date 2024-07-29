from rest_framework import serializers
from .models import Specie,MedEspeciality,Pet,Veterinarian

class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specie
        fields='__all__'

class MedEspecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=MedEspeciality
        fields='__all__'
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pet
        fields='__all__'
        
class VeterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Veterinarian
        fields='__all__'