'''
Exercicio -1 
1- Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(num1, num2, num3):
    result = num1 + num2 + num3
    return result
    
print('Informe tres numero para fazer a Soma:')
print('                                       ')
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segunfo numero: '))
num3 = int(input('Informe o terceito numero: '))
print('                                       ')
print(f'O resultado é = {soma(num1, num2, num3)}')


