#Programa desenvolvido para abrimento de portas eletrônicas
#O programa deve ser utilizado com sensores

from datetime import datetime
now = datetime.now()
cont = 1
entrada = True
while (entrada == True):
    entrada = int(input('Passou alguém? '))
    if(now.hour >= 10 and now.hour <= 16):
        print('Horário de entrada registrado {}, - Abertura da porta OK'.format(now))
        arquivo = open('log.txt', 'w')
        texto = '''
        {}
        {} registradas no expediente
        '''.format(now, cont)
        arquivo.write(texto)
        arquivo.close()
        cont += 1
    else:
        print('Desculpe o transtorno')
        entrada = 0
else:
    now = datetime.now()
    print('Horário de expediente já foi encerrado, volte amanhã!')
