a = int(input())
b = int(input())
c = int(input())

maior_ab = (a + b + abs(a - b)) / 2
maior = (maior_ab + c + abs(maior_ab - c)) / 2

print(f'{maior} eh o maior')