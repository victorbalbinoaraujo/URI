maior = 0
for i in range(0, 10):
    x = int(input())
    if x > maior:
        maior = x
        posicao = i

print(maior)
print(posicao + 1)