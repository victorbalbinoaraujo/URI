x = 1
y = 0
soma = 0
while x != 0:
    x = int(input())
    while y != 5:
        if x % 2 == 0:
            soma += x
            y += 1
        x += 1
    print(soma)
    y = 0
    soma = 0
    