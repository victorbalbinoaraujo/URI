x = int(input())
z = int(input())
cont = 0
soma = 0
while z <= x:
    z = int(input())

for i in range(x, z):
    cont += 1
    soma += i
    if soma > z:
        print(cont)
        break