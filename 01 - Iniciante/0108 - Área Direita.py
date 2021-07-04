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

for i in range(1, 11):
    if i <= 5:
        j = 11
        while i + j >= 12:
            soma += matriz[i][j]
            j -= 1
    else:
        j = 11
        while j > i:
            soma += matriz[i][j]
            j -= 1

if t == 'S':
    print(soma) 
elif t == 'M':
    print(soma / tam)