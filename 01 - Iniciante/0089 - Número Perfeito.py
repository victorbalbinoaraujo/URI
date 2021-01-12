sum = 0
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f"{n} é perfeito.")
    else:
        print(f"{n} não é perfeito.")
    sum = 0