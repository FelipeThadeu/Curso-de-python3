import math

a = float(input('Qual é o ângulo que você deseja: '))
print('O ângulo de: {} \n'
      'O valor da tangente é: {:.2f} \n'
      'O valor do cosseno é: {:.2f} \n'
      'O valor do seno é: {:.2f}'.format(a,math.tan(math.radians(a)),math.cos(math.radians(a)),math.sin(math.radians(a))))