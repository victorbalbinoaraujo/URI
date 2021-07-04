import random

matriz = []
tam = 12
soma = 0

o = str(input()).upper()

for i in range(tam):
    vaux = []
    for j in range(tam):
        vaux.append(round(random.uniform(-100.0, 100.0), 2))
    matriz.append(vaux)
    
# 1 e 10 extremos base Δ
for i in range(1, 11):
    # Até o 5, a área verde é i > j
    if i <= 5:
        j = 0
        while i > j:
            soma += matriz[i][j]
            j += 1
    else:
        j = 0
        # 6,0..4 7,0..3 8,0..2 9,0..1, 10,0
        while i + j <= 10:
            soma += matriz[i][j]
            j += 1

if o == 'S':
    print(soma) 
elif o == 'M':
    print(soma / tam)