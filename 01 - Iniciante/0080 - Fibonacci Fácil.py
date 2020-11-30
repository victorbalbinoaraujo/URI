n = int(input())
nb = 1
nc = 0
i = 1
print(0)
while i < n:
    print(nb)
    na = nb + nc
    nc = nb
    nb = na
    i += 1


