a = float(input())
b = float(input())
c = float(input())
a2 = pow(a, 2)
b2 = pow(b, 2)
c2 = pow(c, 2)

if a >= b + c:
  print('NAO FORMA TRIANGULO')

else:
  if a2 == b2 + c2:
    print('TRIANGULO RETANGULO')
  if a2 > b2 + c2:
    print('TRIANGULO OBTUSANGULO')
  if a2 < b2 + c2:
    print('TRIANGULO ACUTANGULO')
  if a2 == b2 == c2:
    print('TRIANGULO EQUILATERO')
  if (a2 == b2 and b2 != c2) or (a2 == c2 and c2 != b2) or (b2 == c2 and c2 != a2):
    print('TRIANGULO ISOCELES')