distancia = int(input('Digite a distancia: '))
if distancia <= 200:
    print('O valor da sua passagem é: {}'.format(distancia * 0.5))
else:
    print('A distancia é maior que 200km O valor da sua passagem é: {}'.format(distancia * 0.45))