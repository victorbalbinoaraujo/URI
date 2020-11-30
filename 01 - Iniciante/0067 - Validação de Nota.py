media = 0
cont = 0
while cont < 2:
    x = float(input())
    if 0 <= x <= 10:
        media += x
        cont += 1
    else:
        print('nota invalida')

print(f'media = {media / 2}')