inicio = int(input())
fim = int(input())

horas = fim - inicio

if horas <= 0:
  horas += 24

print(f'O JOGO DUROU {horas} HORA(S)')