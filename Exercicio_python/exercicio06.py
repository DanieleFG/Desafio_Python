'''
Exercicio - 6
6- Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas
'''


import random

def escolher_palavra():
    palavras = ["womakerscode", "potencia", "python", "sucesso", "mulher"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("__", end=" ")
    print()

def jogo_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 10
    tentativas = 0
    letras_corretas = set()

    print("-----------------------------")
    print("Bem-vindo ao jogo de Forca!")
    print("-----------------------------")

    while tentativas < tentativas_maximas:
        exibir_palavra(palavra_secreta, letras_corretas)

        print("                                 ")
        letra_tentativa = input("Digite uma letra: ").lower()
        print("                                       ")

        if letra_tentativa in palavra_secreta:
            letras_corretas.add(letra_tentativa)
            print("Letra correta!")
        else:
            print("Letra incorreta!")
            tentativas += 1

        if set(palavra_secreta) == letras_corretas:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == tentativas_maximas:
        print("Você excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)

# Iniciar o jogo
jogo_forca()


