inter = 0
gremio = 0
grenais = 0
empate = 0
x = 0

while x != 2:
    gols_inter = int(input())
    gols_gremio = int(input())
    if gols_inter > gols_gremio:
        inter += 1
    elif gols_gremio > gols_inter:
        gremio += 1
    elif gols_inter == gols_gremio:
        empate += 1
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())

print(f'{grenais} grenais')
print(f'Inter: {inter}')
print(f'Gremio: {gremio}')
print(f'Empates: {empate}')

if inter > gremio:
    print(f'Inter venceu mais')
elif gremio > inter:
    print(f'Gremio venceu mais')
elif inter == gremio:
    print(f'Nao houve vencedor')