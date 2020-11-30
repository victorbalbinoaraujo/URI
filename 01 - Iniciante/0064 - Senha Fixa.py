senha = 2002
x = 0

while x != senha:
    x = int(input())
    if x == senha:
        print('Acesso permitido')
        break
    else:
        print('Acesso negado')