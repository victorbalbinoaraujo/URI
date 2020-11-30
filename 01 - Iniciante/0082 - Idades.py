idade = 1
media_idade = 0
i = 0
while idade > 0:
    idade = int(input())
    if idade > 0:
        media_idade += idade
    i += 1

print(f'{media_idade / (i - 1)}')