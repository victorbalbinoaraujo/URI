def fibonacci(num):
    aa = 0
    a = 1
    soma = 0
    for _ in range(1, num):
        soma = aa + a
        aa = a
        a = soma
    return soma

teste = int(input())

for _ in range(teste):
    n = int(input())
    print(f"Fib({n}) = {fibonacci(n)}")
