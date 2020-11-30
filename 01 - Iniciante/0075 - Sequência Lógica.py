n = int(input())
x = 1

for i in range(n):
    print(f'{x} {x ** 2} {x ** 3}')
    print(f'{x} {x ** 2 + 1} {x ** 3 + 1}')
    x += 1