alcool = 0
gasolina = 0
diesel = 0

while True:
    produtos = int(input())
    if produtos == 1:
        alcool += 1
    elif produtos == 2:
        gasolina += 1
    elif produtos == 3:
        diesel += 1
    elif produtos == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')