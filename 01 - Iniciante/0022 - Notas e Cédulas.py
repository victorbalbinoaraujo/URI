dinheiro = float(input())
aux = dinheiro
y = (dinheiro - int(aux)) * 100 + 0.1
aux2 = y
print(f'{int(dinheiro / 100)} nota(s) de R$ 100.00')
aux = dinheiro % 100
print(f'{int(aux / 50)} nota(s) de R$ 50.00')
aux %= 50
print(f'{int(aux / 20)} nota(s) de R$ 20.00')
aux %= 20
print(f'{int(aux / 10)} nota(s) de R$ 10.00')
aux %= 10
print(f'{int(aux / 5)} nota(s) de R$ 5.00')
aux %= 5
print(f'{int(aux / 2)} nota(s) de R$ 2.00')
aux %= 2
print(f'{int(aux / 1)} moeda(s) de R$ 1.00')
aux %= 1
print(f'{int(y / 50)} moeda(s) de R$ 0.50')
aux2 %= 50
print(f'{int(aux2 / 25)} moeda(s) de R$ 0.25')
aux2 %= 25
print(f'{int(aux2 / 10)} moeda(s) de R$ 0.10')
aux2 %= 10
print(f'{int(aux2 / 5)} moeda(s) de R$ 0.05')
aux2 %= 5
print(f'{int(aux2 / 1)} moeda(s) de R$ 0.01')
aux2 %= 1