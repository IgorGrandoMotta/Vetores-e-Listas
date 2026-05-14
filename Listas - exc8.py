lista = []

for i in range(1, 11):
    lista.append(i * i)

soma = 0
for numero in lista:
    soma = soma + numero

print("Lista:", lista)
print("Soma:", soma)