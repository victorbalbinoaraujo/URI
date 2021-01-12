valor = int(input())
vetor = [x * 2 for x in range(valor, 10)]
print(f"N[0] = {valor}")
for i, v in enumerate(vetor):
    i += 1
    print(f"N[{i}] = {v}")