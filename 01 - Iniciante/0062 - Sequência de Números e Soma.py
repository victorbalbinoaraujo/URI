x = 1
y = 1
soma = 0
while True:
    x = int(input())
    y = int(input())
    if x <= 0 or y <= 0:
        break
    for i in range(y, x + 1):
        soma += i
    print(f'Sum = {soma}')
    soma = 0