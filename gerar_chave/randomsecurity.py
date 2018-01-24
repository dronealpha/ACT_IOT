from random import choice


def gera_senha(tamanho):
    caracters = '0123456789abcdefghijlmnopqrstuwvxz' 
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)
    return senha
         
print gera_senha(3)