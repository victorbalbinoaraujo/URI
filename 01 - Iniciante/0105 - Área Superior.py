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

for i in range(4):
    for j in range(i + 1, 10 - i):
        print(matriz[i][j])
        soma += matriz[i][j]


if t == 'S':
    print(soma) 
elif t == 'M':
    print(soma / tam)



