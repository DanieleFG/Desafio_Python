'''
Exercicio - 5
5- Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''


def contarVogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0

    for char in frase:
        if char in vogais:
            contador += 1

    return contador

frase_usuario = input("Digite uma frase: ")

total_vogais = contarVogais(frase_usuario)
print(f"O total de vogais na frase é: {total_vogais}")



