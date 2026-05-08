lista = list()
i = 1

print("Digite 5 vezes qualquer valor inteiro e positivo.")
for i in range(1,6):
    valor = int(input("Valor:"))
    lista.append(valor)
print("")

lista2 = sorted(lista)
lista3 = sorted(lista, reverse=True)

print("Lista:",lista,"\n")
print("Lista em forma ordenada:",lista2,"\n")
print("Lista em ordem decrescente:",lista3,"\n")
print("Menor valor da lista:",min(lista),"\n")
print("Maior valor da lista:",max(lista),"\n")
print("Soma dos valores da lista:",sum(lista),"\n")
      