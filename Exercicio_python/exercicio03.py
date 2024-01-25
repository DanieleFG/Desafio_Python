'''
Exercicio - 3
3- Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função..
'''

def convertCelsius(num1):
    result = (num1 - 32) / 1.8
    return result


def convertFahren(num1):
    result = num1 * 1.8 + 32
    return result
    

print('                                       ')
num1 = float(input('Informe uma temperatura: '))
print('                                     ')
print('Escolha uma opção que deseja converter:')
print('---------------------------------------')
print('[ c ] - para Celsius:')
print('[ f ] - para Fahrenheit:')
print('---------------------------------------')
medida = input('c ou f ? ')

if medida == 'c':
    result = convertCelsius(num1)
    print('                                       ')
    print(f'A temperatura em Celsius {result:.1f}° C')
elif medida == 'f':
    result =convertFahren(num1)
    print('                                       ')
    print(f'A temperatura em Fahrenheit {result:.1f}° F')
else:
    print('Opção Invalida!!')



