x = int(input())
y = int(input())
i = 1
cont = 0
while i <= y:
    print(i)
    cont += 1
    if cont == x:
        print()
        cont = 0
    i += 1