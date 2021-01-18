vetor = [int(input()) for _ in range(5)]
vetor.reverse()
for i, item in enumerate(vetor):
    print(f"N[{i}] = {item}")