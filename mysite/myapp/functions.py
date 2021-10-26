import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    extensao = os.path.splitext(value.name)
    extensao_valida = 'txt'
    if not extensao.lower() == extensao_valida:
        raise ValidationError('Tipo de arquivo não suportado.')



