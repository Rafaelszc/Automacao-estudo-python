import re

senhav1, senhav2, senhav3 = re.compile('[a-z]+'), re.compile('[A-Z]+'), re.compile('[1-9]+')

def verificar(senha):
    if len(senha) < 8:
        return print('Senha reprovada, sua senha deve ter no mínimo 8 caracteres!')
    elif re.findall(senhav1, senha) == []:
        return print('Senha reprovada, insira pelo menos uma letra minúscula!')

    elif re.findall(senhav2, senha) == []:
        return print('Senha reprovada, insira pelo menos uma letra maiúscula!')

    elif re.findall(senhav3, senha) == []:
        return print('Senha reprovada, insira pelo menos um número!')
    
    return print('Senha aprovada!')