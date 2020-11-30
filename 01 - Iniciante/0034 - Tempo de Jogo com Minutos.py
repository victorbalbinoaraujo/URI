horas1 = int(input())
min1 = int(input())
horas2 = int(input())
min2 = int(input())

tempo1 = horas1 * 60 + min1
tempo2 = horas2 * 60 + min2

if tempo2 > tempo1:
  aux = tempo2 - tempo1
else:
  aux = tempo2 - tempo1 + 24 * 60

horas = aux / 60
minutos = aux % 60

print(f'O JOGO DUROU {int(horas)} HORA(S) E {int(minutos)} MINUTO(S)')