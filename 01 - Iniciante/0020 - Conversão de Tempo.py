horario = int(input())
segundos = horario % 60
minutos = (horario / 60) % 60
horas = horario / 3600

print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')