'''
Exercicio - 4
4- Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo
'''
def converterDolarAmericano(valor):
    if valor > 4.91: 
        result = valor / 4.91
        print(f'Valor do cambio do  Dolar Americano {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Dolar Americano')

def converterPesoArgentino(valor):
    if valor > 0.02: 
        result = valor / 0.02
        print(f'Valor do cambio do  Peso Argentino {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Peso Argentino')

def converterDolarAustraliano(valor):
    if valor > 3.18: 
        result = valor / 3.18
        print(f'Valor do cambio do Dolar Australiano {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Dolar Australiano')

def converterDolarCanadense(valor):
    if valor > 3.64: 
        result = valor / 3.64
        print(f'Valor do cambio do Dolar Canadense {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Dolar Canadense')

def converterFrancoSuico(valor):
    if valor > 0.42: 
        result = valor / 0.42
        print(f'Valor do cambio do Franco Suiço {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Franco Suiço')

def converterEuro(valor):
    if valor > 5.36: 
        result = valor / 5.36
        print(f'Valor do cambio do Euro {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Euro')

def converterLibraEsterlina(valor):
    if valor > 6.21: 
        result = valor / 6.21
        print(f'Valor do cambio do Libra Esterlina {result:.2f}')
    else: 
        print('Valor da carteira inferior ao Libra Esterlina')
        
#Libra esterlina

print('                                       ')
print('------------------------------------------------')
valor = float(input('Informe o valor que possui na carteira: '))
print('------------------------------------------------')
converterDolarAmericano(valor)
converterPesoArgentino(valor)
converterDolarAustraliano(valor)
converterDolarCanadense(valor)
converterLibraEsterlina(valor)
converterEuro(valor)
converterFrancoSuico(valor)





