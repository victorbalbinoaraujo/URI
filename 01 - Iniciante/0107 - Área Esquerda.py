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

for i in range(1, 10):
    if i <= 5:
        for j in range(j < i):
            soma += matriz[i][j]
    else:
        for j in range(11 - i):
            soma += matriz[i][j]

if t == 'S':
    print(soma) 
elif t == 'M':
    print(soma / tam)