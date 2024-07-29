from django.db import models
from .validators import	validate_age, validate_number, validate_no_numbers, validate_no_symbols, validate_max_two_words

# Create your models here.
class Specie(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_no_numbers, validate_no_symbols, validate_max_two_words])

    def __str__(self):
        return self.name


class MedEspeciality(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_no_numbers, validate_no_symbols, validate_max_two_words])

    def __str__(self):
        return self.name

class Veterinarian(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_no_numbers, validate_no_symbols, validate_max_two_words])
    medespeciality = models.ForeignKey(MedEspeciality, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100, validators=[validate_no_numbers, validate_no_symbols, validate_max_two_words])
    owner = models.CharField(max_length=100)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    history = models.TextField()
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[validate_age, validate_number])
    weight = models.DecimalField(max_digits=4, decimal_places=2, validators=[validate_number])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name