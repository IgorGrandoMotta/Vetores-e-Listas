lista = list()
i = 1

print("Digite 5 vezes qualquer valor inteiro e positivo.")
while i < 6:
    try:
        valor = int(input("Valor:"))
        if valor >= 0:
            lista.append(valor)
            i += 1
        else:
            print("Você Digitou um valor que não é positivo, tente novamente.")
    except ValueError:
        print("Você digitou um valor não inteiro, tente novamente.")
print("")

lista2 = sorted(lista)
lista3 = sorted(lista, reverse=True)

print("Lista:",lista,"\n")
print("Lista em forma ordenada:",lista2,"\n")
print("Lista em ordem decrescente:",lista3,"\n")
print("O tamanho da lista é de",len(lista),"números.""\n")
print("Menor valor da lista:",min(lista),"\n")
print("Maior valor da lista:",max(lista),"\n")
print("Soma dos valores da lista:",sum(lista),"\n")
      