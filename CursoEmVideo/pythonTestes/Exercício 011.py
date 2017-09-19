largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
a = largura * altura
litros = a / 2

print ('Sua parede tem a dimensão de {}X{} e sua área é de {}m²\n ' 
       'Para pintar sua parede é necessário {} litros de tinta'.format(largura, altura, a, litros))