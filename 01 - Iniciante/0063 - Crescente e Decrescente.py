x = 1
y = 0

while x != y:
    x = int(input())
    y = int(input())
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')