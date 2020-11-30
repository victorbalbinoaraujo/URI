n = int(input())
i = 0
dentro = 0
fora = 0

while i < n:
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
    i += 1

print(f'{dentro} in')
print(f'{fora} out')