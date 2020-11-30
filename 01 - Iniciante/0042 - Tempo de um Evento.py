diaI = int(input())
horasI = int(input())
minutosI = int(input())
segundosI = int(input())
diaF = int(input())
horasF = int(input())
minutosF = int(input())
segundosF = int(input())

tempo1 = ((diaI * 24 + horasI) * 60 + minutosI) * 60 + segundosI
tempo2 = ((diaF * 24 + horasF) * 60 + minutosF) * 60 + segundosF

aux = tempo2 - tempo1

dias = aux / (24 * 3600)
horas = aux % (24 * 3600) / 3600
minutos = aux % 3600 / 60
segundos = aux % 60

print(f'{int(dias)} dia(s)')
print(f'{int(horas)} hora(s)')
print(f'{int(minutos)} minuto(s)')
print(f'{int(segundos)} segundo(s)')