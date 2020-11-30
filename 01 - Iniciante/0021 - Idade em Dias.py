idade_em_dias = int(input())

print(f'{int(idade_em_dias / 365)} ano(s)')
idade_em_dias %= 365
print(f'{int(idade_em_dias / 30)} mes(es)')
idade_em_dias %= 30
print(f'{int(idade_em_dias)} dia(s)')