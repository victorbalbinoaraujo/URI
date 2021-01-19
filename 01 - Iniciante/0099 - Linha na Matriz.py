import random

matriz = []

for i in range(12):
    vaux = []
    for j in range(12):
        vaux.append(round(random.uniform(-100.00, 100.00), 2))
    matriz.append(vaux)

l = int(input())
t = str(input()).upper()
soma = 0

for i in range(12):
    for j in range(12):
        if l == i:
            print(matriz[i][j])
            soma += matriz[i][j]

if t == 'S':
    print(soma)
elif t == 'M':
    print(soma / 12)
