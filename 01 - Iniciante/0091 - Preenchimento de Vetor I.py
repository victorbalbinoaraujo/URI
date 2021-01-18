valor = int(input())
n = []
n.append(valor)
for _ in range(10):
    valor *= 2
    n.append(valor)

for i, item in enumerate(n):
    print(f"N[{i}] = {item}")