import math

a = float(input())
b = float(input())
c = float(input())


delta = ((pow(b, 2)) - (4 * a * c))

x1 = (- b + math.sqrt(delta)) / (2 * a)
x2 = (- b - math.sqrt(delta)) / (2 * a)

if a == 0 or delta < 0:
  print('Impossivel calcular')
else:
  print(f'R1 = {x1}')
  print(f'R2 = {x2}')