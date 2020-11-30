i = 0.0
j = 1.0

while i <= 2:
    print(f'I = {i} J = {j}')
    if int(j) - int(i) == 3:
        i += 0.2
        j -= 1.8
    else:
        j += 1