n = int(input())
i = 0
while i < n:
    x = int(input())
    y = int(input())
    if y != 0:
        print(x / y)
    else:
        print('divisao impossivel')
    i += 1