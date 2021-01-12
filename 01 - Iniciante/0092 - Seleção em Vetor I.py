numeros = [float(input()) for _ in range(100)]
for numero in numeros:
    if numero < 10:
        print(f"A[{numeros.index(numero)}] = {numero}")