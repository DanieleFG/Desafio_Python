'''
Exercicio - 
2- Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado. Porexemplo:127->721.
'''

def reverso(num1):
    result = num1[::-1]
    return result
    

print('                                       ')
num1 = (input('Informe o um numero e retornarei o reserso dele: '))

print('                                       ')
print(f'O reverso é = {reverso(num1)}')


