a = float(input())
b = float(input())
c = float(input())

if a < b + c and b < a + c and c < a + b:
  print(f'Perimetro: {a + b + c}')
else:
  print(f'Area: {(a + b) * c / 2}')