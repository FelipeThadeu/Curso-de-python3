dias = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quantos kilometros você rodou com o carro? '))

print('O valor a ser pago pela diária é: {}'.format(dias * 60 + km * 0.15))