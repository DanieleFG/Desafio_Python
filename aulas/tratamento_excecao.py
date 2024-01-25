def divisao(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print('Impossivel dividir por zero')


num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

print(divisao(num1, num2))