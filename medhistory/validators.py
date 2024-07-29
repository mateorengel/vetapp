from django.core.exceptions import ValidationError
import re

def validate_age(value):
    if value > 30:
        raise ValidationError('Age must be less than 30.')
    
def validate_number(value):
    if value < 0:
        raise ValidationError('Number must be greater than 0.')
    
def validate_no_numbers(value):
    if re.search(r'\d', value):
        raise ValidationError('Numbers are not allowed in this field.')
    
def validate_no_symbols(value):
    if not re.match(r'^[\w\s]*$', value):
        raise ValidationError('Symbols are not allowed in this field.')

def validate_max_two_words(value):
    words = value.split()
    if len(words) > 2:
        raise ValidationError('Max two words in this field.')