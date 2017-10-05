n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))

if n1 > n2:
    print('Número 1 = {} é maior que o número 2'.format(n1))
elif n1 == n2:
    print('Os números são iguais')
elif n1 < n2:
    print('Número 2 = {} é maior'.format(n2))
