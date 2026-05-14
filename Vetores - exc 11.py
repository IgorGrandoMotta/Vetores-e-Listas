A = [0, 0, 0, 0, 0]

A[0] = float(input("Valor 1: "))
A[1] = float(input("Valor 2: "))
A[2] = float(input("Valor 3: "))
A[3] = float(input("Valor 4: "))
A[4] = float(input("Valor 5: "))

maior = A[0]
posicao_maior = 0
if A[1] > maior:
    maior = A[1]
    posicao_maior = 1
if A[2] > maior:
    maior = A[2]
    posicao_maior = 2
if A[3] > maior:
    maior = A[3]
    posicao_maior = 3
if A[4] > maior:
    maior = A[4]
    posicao_maior = 4

menor = A[0]
posicao_menor = 0
if A[1] < menor:
    menor = A[1]
    posicao_menor = 1
if A[2] < menor:
    menor = A[2]
    posicao_menor = 2
if A[3] < menor:
    menor = A[3]
    posicao_menor = 3
if A[4] < menor:
    menor = A[4]
    posicao_menor = 4

print("Maior valor:", maior, "- Posição:", posicao_maior)
print("Menor valor:", menor, "- Posição:", posicao_menor)