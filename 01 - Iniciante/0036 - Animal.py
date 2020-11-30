primeira = str(input())
segunda = str(input())
terceira = str(input())

if primeira == 'vertebrado':
  if segunda == 'ave':
    if terceira == 'carnivoro':
      print('aguia')
    elif terceira == 'onivoro':
      print('pomba')
  elif segunda == 'mamifero':
      if terceira == 'onivoro':
        print('homem')
      elif terceira == 'herbivoro':
        print('vaca')
elif primeira == 'invertebrado':
  if segunda == 'inseto':
    if terceira == 'hematofogo':
      print('pulga')
    elif terceira == 'herbivoro':
      print('lagarta')
  elif segunda == 'anelideo':
      if terceira == 'hematofogo':
        print('sanguessuga')
      elif terceira == 'onivoro':
        print('minhoca')