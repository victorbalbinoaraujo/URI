nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + nota4) / 10

if 5 <= media <= 6.9:
  print('Aluno em exame')
  exame = float(input('Nota do exame: '))
  media = (media + exame) / 2
  if media > 5:
    print('Aluno aprovado')
    print(f'Media final: {media}')
  else:
    print('Aluno reprovado')
    print(f'Media final: {media}')
elif media > 7:
  print('ALuno aprovado')
  print(f'Media final: {media}')
else:
  print('Aluno reprovado')
  print(f'Media final: {media}')