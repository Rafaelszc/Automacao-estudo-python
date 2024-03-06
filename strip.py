import re

def strip(string, arg):
    texto = re.compile(f'[ {arg}]+')
    return texto.sub('', string)