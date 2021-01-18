t = int(input())
n = []
j = 0
i = 0
for i in range(1000):
    n.append(j)
    print(f"N[{i}] = {j}")
    if j < t-1:
        j += 1
    else:
        j = t-1
        j = 0
    i += 1