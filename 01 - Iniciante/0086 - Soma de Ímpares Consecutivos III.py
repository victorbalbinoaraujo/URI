n = int(input())
soma = 0
j = 0
for i in range(n):
    x = int(input())
    y = int(input())
    while j != y:
        if x % 2 == 1:
            j += 1
            soma += x
        x += 1
    print(soma)
    soma = 0
    j = 0