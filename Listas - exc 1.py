import random
numerosJogador1 = list()
numerosJogador2 = list()
i = 1

print("-----Jogador 1-----")
for i in range(1,4):
    valor = random.randint(1,6)
    numerosJogador1.append(valor)
    print("Valor do",i,"dado:",valor)
print("Soma dos dados:",sum(numerosJogador1),"\n")

print("-----Jogador 2-----")
for i in range(1,4):
    valor = random.randint(1,6)
    numerosJogador2.append(valor)
    print("Valor do",i,"dado:",valor)
print("Soma dos dados:",sum(numerosJogador2),"\n")
