import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(alfabeto)

print("O alfabeto foi embaralhado!")

letra = input("Digite uma letra para adivinhar a posição (0 a 25): ")
posicao = int(input("Em qual posição você acha que ela está? "))

if alfabeto[posicao] == letra:
    print("Acertou! A letra", letra, "está na posição", posicao)
else:
    print("Errou! A letra", letra, "está na posição", alfabeto.index(letra))