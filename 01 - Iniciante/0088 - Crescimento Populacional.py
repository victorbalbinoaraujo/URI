teste = int(input())
tempo = 0
for i in range(0, teste):
    pa = int(input())
    pb = int(input())
    g1 = float(input())
    g2 = float(input())
    while pa <= pb:
        pa += int(pa * g1 / 100)
        pb += int(pb * g2 / 100)
        tempo += 1
    if tempo > 100:
        print('Mais de 1 século...')
    else:
        print(f'{tempo} ano(s).')
    tempo = 0