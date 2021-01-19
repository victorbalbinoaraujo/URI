x = float(input())
n = []
n.append(x)

for _ in range(99):
    x /= 2
    n.append(x)

for i, item in enumerate(n):
    print(f"N[{i}] = {item}")