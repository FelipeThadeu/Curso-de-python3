from random import randint
import time
numero = input("Digite um numero entre 0 e 5: ")
n = randint(0, 5)
print('processando...')
time.sleep(2)
if numero == n:
    print('Acertou!')
else:
    print('Tente novamente, eu escolhi {}'.format(n))

