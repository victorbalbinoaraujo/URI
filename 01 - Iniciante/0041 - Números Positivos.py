positivos = 0
for i in range(6):
  x = int(input())
  if x > 0:
    positivos += 1

print(f'{positivos} valores positivos')