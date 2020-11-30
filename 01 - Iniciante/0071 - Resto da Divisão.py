x = int(input())
y = int(input())
aux = 0

if x > y:
    aux = x
    x = y
    y = aux
    print(x)
    print(y)
for i in range(x, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)