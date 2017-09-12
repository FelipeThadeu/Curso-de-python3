import random
a1 = input('Digite o 1° alunos: ')
a2 = input('Digite o 2° alunos: ')
a3 = input('Digite o 3° alunos: ')
a4 = input('Digite o 4° alunos: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
