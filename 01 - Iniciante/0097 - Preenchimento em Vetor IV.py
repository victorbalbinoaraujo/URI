par = []
impar = []
c = 0
for _ in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
        print(f"par[{c}] = {x}")
        c += 1
        if c == 5:
            c = 0
    else:
        impar.append(x)
        print(f"impar[{c}] = {x}")
        c += 1
        if c == 5:
            c = 0