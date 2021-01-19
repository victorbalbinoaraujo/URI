import random

matriz = []
tam = 12
for i in range(tam):
    vaux = []
    for j in range(tam):
        vaux.append(round(random.uniform(-100.0, 100.0), 2))
    matriz.append(vaux)

t = str(input()).upper()
soma = 0

for i in range(tam):
    for j in range(tam):
        if i > j:
            print(matriz[i][j])
            soma += matriz[i][j]

if t == 'S':
    print(soma) 
elif t == 'M':
    print(soma / tam)