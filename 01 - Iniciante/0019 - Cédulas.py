dinheiro = int(input())
print(f'{dinheiro / 100} notas de R$ 100.00')
aux = dinheiro % 100
print(f'{aux / 50} notas de R$ 50.00')
aux %= 50
print(f'{aux / 20} notas de R$ 20.00')
aux %= 20
print(f'{aux / 10} notas de R$ 10.00')
aux %= 10
print(f'{aux / 5} notas de R$ 5.00')
aux %= 5
print(f'{aux / 2} notas de R$ 2.00')
aux %= 2
print(f'{aux / 1} notas de R$ 1.00')