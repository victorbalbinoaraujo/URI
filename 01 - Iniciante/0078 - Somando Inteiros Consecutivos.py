a = int(input())
n = int(input())
soma = 0

while n <= 0:
    n = int(input())


for i in range(0, n):
    soma += (a + i)

print(soma)