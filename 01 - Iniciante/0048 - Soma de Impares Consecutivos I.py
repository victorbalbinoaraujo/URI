fim = int(input())
inicio = int(input())
soma = 0

for i in range(inicio, fim):
    if abs(i) % 2 == 1:
        if i != inicio:
            soma += i

print(soma)
