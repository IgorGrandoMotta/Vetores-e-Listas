A = [0, 0, 0, 0, 0]

A[0] = float(input("Valor 1: "))
A[1] = float(input("Valor 2: "))
A[2] = float(input("Valor 3: "))
A[3] = float(input("Valor 4: "))
A[4] = float(input("Valor 5: "))

maior = A[0]
if A[1] > maior:
    maior = A[1]
if A[2] > maior:
    maior = A[2]
if A[3] > maior:
    maior = A[3]
if A[4] > maior:
    maior = A[4]

menor = A[0]
if A[1] < menor:
    menor = A[1]
if A[2] < menor:
    menor = A[2]
if A[3] < menor:
    menor = A[3]
if A[4] < menor:
    menor = A[4]

media = (A[0] + A[1] + A[2] + A[3] + A[4]) / 5

print("Valores:", A[0], A[1], A[2], A[3], A[4])
print("Maior:", maior)
print("Menor:", menor)
print("Média:", media)