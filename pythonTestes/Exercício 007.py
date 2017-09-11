n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >=6:
    print('A sua média é: {}, você foi aprovado!'.format(m))
else:
    print('A sua média é: {}, você foi reprovado!'.format(m))

