lista = list(range(1, 101))

pares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)