casos_de_teste = int(input())
total_animais = 0
total_ratos = 0
total_coelhos = 0
total_sapos = 0

for i in range(0, casos_de_teste):
    quantidade = int(input())
    animal = str(input())
    if animal == 'R':
        total_ratos += quantidade
    elif animal == 'C':
        total_coelhos += quantidade
    elif animal == 'S':
        total_sapos += quantidade
    total_animais += quantidade

print(f'Total: {total_animais}')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total ratos: {total_ratos}')
print(f'Total sapos: {total_sapos}')

percentual_coelhos = (total_coelhos * 100) / total_animais
percentual_ratos = (total_ratos *  100) / total_animais
percentual_sapos = (total_sapos * 100) / total_animais

print(f'Percentual de coelhos: {percentual_coelhos}%')
print(f'Percentual de ratos: {percentual_ratos}%')
print(f'Percentual de sapos: {percentual_sapos}%')