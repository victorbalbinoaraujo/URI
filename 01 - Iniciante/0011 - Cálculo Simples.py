codigo_peca1 = int(input())
numero_peca1 = int(input())
valor_peca1 = float(input())
codigo_peca2 = int(input())
numero_peca2 = int(input())
valor_peca2 = float(input())

preco = (numero_peca1 * valor_peca1) + (numero_peca2 * valor_peca2)
print(f'VALOR A PAGAR: R${preco}')