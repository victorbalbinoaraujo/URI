import random

matriz = []
tam = 12
soma = 0
t = str(input()).upper()
for i in range(tam):
    vaux = []
    for j in range(tam):
        vaux.append(round(random.uniform(-100.0, 100.0), 2))
    matriz.append(vaux)

for i in range(7, 11):
    for j in range(11 - i + 1, i - 1):
        soma += matriz[i][j]


if t == 'S':
    print(soma) 
elif t == 'M':
    print(soma / tam)