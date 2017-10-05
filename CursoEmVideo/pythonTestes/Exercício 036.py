vcasa = float(input("Digite a valor da casa: "))
sal = float(input("Digite a valor do salário: "))
tmp = float(input("Digite o tempo que deseja pagar em anos: "))

juros = vcasa * (tmp * 0.02)
mens = ((vcasa + juros)/(tmp * 12))


if mens > (sal * 0.3):
    print('Desculpa, mas infelizmente a mensalidade ultrapassou 30% do seu salário, \n'
          'não podemos liberar o financiamento, o valor ficaria de {:2f}'.format(mens))
elif mens < (sal * 0.3):
    print('O seu cadastro foi aprovado! em {} prestações no valor de {:2f}'.format(tmp * 12,mens))
