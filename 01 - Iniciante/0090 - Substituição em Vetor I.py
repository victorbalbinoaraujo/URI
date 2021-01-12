numeros = [int(input()) for _ in range(5)]
for i, numero in enumerate(numeros):
    if numero <= 0:
        numero = 1
    print(f"x[{i}] = {numero}")