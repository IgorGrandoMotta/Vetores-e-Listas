A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

A[0] = int(input("Valor 1: "))
A[1] = int(input("Valor 2: "))
A[2] = int(input("Valor 3: "))
A[3] = int(input("Valor 4: "))
A[4] = int(input("Valor 5: "))
A[5] = int(input("Valor 6: "))
A[6] = int(input("Valor 7: "))
A[7] = int(input("Valor 8: "))
A[8] = int(input("Valor 9: "))
A[9] = int(input("Valor 10: "))

maior = A[0]

if A[1] > maior:
    maior = A[1]
if A[2] > maior:
    maior = A[2]
if A[3] > maior:
    maior = A[3]
if A[4] > maior:
    maior = A[4]
if A[5] > maior:
    maior = A[5]
if A[6] > maior:
    maior = A[6]
if A[7] > maior:
    maior = A[7]
if A[8] > maior:
    maior = A[8]
if A[9] > maior:
    maior = A[9]

menor = A[0]

if A[1] < menor:
    menor = A[1]
if A[2] < menor:
    menor = A[2]
if A[3] < menor:
    menor = A[3]
if A[4] < menor:
    menor = A[4]
if A[5] < menor:
    menor = A[5]
if A[6] < menor:
    menor = A[6]
if A[7] < menor:
    menor = A[7]
if A[8] < menor:
    menor = A[8]
if A[9] < menor:
    menor = A[9]

print("")
print("Maior:", maior)
print("")
print("Menor:", menor)