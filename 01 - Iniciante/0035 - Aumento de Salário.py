salario = float(input())

if 0 < salario <= 400.00:
  novo_salario = salario + (salario  * 0.15)
  reajuste = novo_salario - salario
  percentual = 15
elif 400.01 <= salario <= 800.00:
  novo_salario = salario + (salario  * 0.12)
  reajuste = novo_salario - salario
  percentual = 12
elif 800.01 <= salario <= 1200.00:
  novo_salario = salario + (salario  * 0.10)
  reajuste = novo_salario - salario
  percentual = 10
elif 1200.01 <= salario <= 2000.00:
  novo_salario = salario + (salario  * 0.07)
  reajuste = novo_salario - salario
  percentual = 7
elif salario > 2000.00:
  novo_salario = salario + (salario  * 0.04)
  reajuste = novo_salario - salario
  percentual = 4

print(f'Novo salario: {novo_salario}')
print(f'Reajuste ganho: {reajuste}')
print(f'Em percentual {percentual} %')