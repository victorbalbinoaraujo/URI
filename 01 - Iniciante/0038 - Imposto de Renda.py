dinheiro = float(input())

if dinheiro <= 2000.00:
  print('Isento')
elif 2000.01 < dinheiro < 3000.00:
  dinheiro = (dinheiro - 2000) * 0.08
elif 3000.01 < dinheiro < 4500.00:
  dinheiro = (1000 * 0.08) + (dinheiro - 3000) * 0.18
elif dinheiro > 4500:
  dinheiro = (1000 * 0.08) +(1500 * 0.18) + ((dinheiro - 4500) * 0.28)

print(f'R$ {dinheiro}')