f = input('Digite a frase: ').strip().lower()
print('A letra A aparece {} vezes na frase. \n'
      'A primeira letra A apareceu na posição {}. \n'
      'A última posição da letra A é {}.'.format(f.count('a'), f.find('a')+1, f.rfind('a')+1))