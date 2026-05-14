A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

A[0] = float(input("Valor 1: "))
A[1] = float(input("Valor 2: "))
A[2] = float(input("Valor 3: "))
A[3] = float(input("Valor 4: "))
A[4] = float(input("Valor 5: "))
A[5] = float(input("Valor 6: "))
A[6] = float(input("Valor 7: "))
A[7] = float(input("Valor 8: "))
A[8] = float(input("Valor 9: "))
A[9] = float(input("Valor 10: "))

quantidade_negativos = 0
soma_positivos = 0

if A[0] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[0] > 0:
    soma_positivos = soma_positivos + A[0]

if A[1] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[1] > 0:
    soma_positivos = soma_positivos + A[1]

if A[2] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[2] > 0:
    soma_positivos = soma_positivos + A[2]

if A[3] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[3] > 0:
    soma_positivos = soma_positivos + A[3]

if A[4] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[4] > 0:
    soma_positivos = soma_positivos + A[4]

if A[5] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[5] > 0:
    soma_positivos = soma_positivos + A[5]

if A[6] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[6] > 0:
    soma_positivos = soma_positivos + A[6]

if A[7] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[7] > 0:
    soma_positivos = soma_positivos + A[7]

if A[8] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[8] > 0:
    soma_positivos = soma_positivos + A[8]

if A[9] < 0:
    quantidade_negativos = quantidade_negativos + 1
if A[9] > 0:
    soma_positivos = soma_positivos + A[9]

print("Quantidade de negativos:", quantidade_negativos)
print("Soma dos positivos:", soma_positivos)