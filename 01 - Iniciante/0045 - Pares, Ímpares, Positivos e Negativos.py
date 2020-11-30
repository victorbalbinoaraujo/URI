pares = 0
positivos = 0
impares = 0
negativos = 0

for i in range(5):
    x = int(input())
    if x > 0:
        positivos += 1
    else:
        negativos += 1
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'{pares} valores par(es)')
print(f'{impares} valores impar(es)')
print(f'{positivos} valores positivo(s)')
print(f'{negativos} valores negativo(s)')