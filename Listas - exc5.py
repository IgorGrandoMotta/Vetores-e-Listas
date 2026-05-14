lista = ["banana", "uva", "melancia", "kiwi", "morango"]

mais_longa = ""
mais_curta = lista[0]

for palavra in lista:
    if len(palavra) > len(mais_longa):
        mais_longa = palavra
    if len(palavra) < len(mais_curta):
        mais_curta = palavra

print("Mais longa:", mais_longa)
print("Mais curta:", mais_curta)