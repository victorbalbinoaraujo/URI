n = int(input())
cont = 0
soma = 0
while cont < n:
    x = int(input())
    y = int(input())
    for i in range(x + 1, y):
        if i % 2 == 1:
            soma += i
    print(soma)
    soma = 0
    cont += 1