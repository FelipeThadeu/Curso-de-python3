import datetime

dia = int(input('Digite o dia de nascimento: '))
mes = int(input('Digite o mês de nascimento: '))
ano = int(input('Digite o ano de nascimento: '))

atualano = datetime.date(year)
tmpano = ano - atualano
print (tmpano)