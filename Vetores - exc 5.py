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

par = 0
i = 0
for i in range(10):
    if A[i] % 2 == 0:
        par += 1

print("A quantidade de numeros pares na lista é:",par)