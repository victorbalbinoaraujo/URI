media = 0
cont = 0
opt = 0
while opt != 2:
    x = float(input())
    if 0 <= x <= 10:
        media += x
        cont += 1
        if cont == 2:
            print(f'media = {media / 2}')
    else:
        print('nota invalida')
    while opt != 2 and cont == 2:
        print('novo calculo (1-sim 2-nao)')
        opt = int(input())
        if opt == 1:
            cont = 0
            media = 0
            break