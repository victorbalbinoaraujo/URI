soma = 0
j = 1
k = 1
for i in range(20):
    soma += j / k
    j += 2
    k += k
print(soma)