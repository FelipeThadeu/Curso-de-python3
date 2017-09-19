v = float(input('Qual é sua velocidade? '))
if v >= 81:
    print('Você foi multado no valor de: \033[1;31m{:.2f}\033[m'.format((v-80)*7))
else:
    print('\033[1;32;mParabéns\033[m você não ultrapassou o limite de 80km/h, continue assim!')