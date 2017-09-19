preco = float(input('Qual é o valor do produto? '))
desconto = int(input('Entre os descontos de 5%, 10%, 20% e 30%, qual será? '))
if desconto == 5:
     print('O produto com 5% de desconto é {}'.format(preco*0.95))
elif desconto == 10:
     print('O produto com 10% de desconto é {}'.format(preco * 0.9))
elif desconto == 20:
     print('O produto com 20% de desconto é {}'.format(preco * 0.8))
elif desconto == 30:
     print('O produto com 30% de desconto é {}'.format(preco * 0.7))
