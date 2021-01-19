tam = int(input())
xv = [int(input()) for _ in range(tam)]
menor = min(xv)
posicao = xv.index(menor)
print(f"Menor valor: {menor}")
print(f"Posição: {posicao}")