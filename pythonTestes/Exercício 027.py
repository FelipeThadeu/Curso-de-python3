nome = input('Digite o nome completo: ').strip()
n = nome.split()
print('O primeiro nome é: {} \n'
      'O ultimo nome é: {}'.format(n[0], n[len(n)-1]))
