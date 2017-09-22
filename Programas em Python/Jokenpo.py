resp = input('Deseja jogar Jokenpo? ')
while resp.lower() == 'sim':
    jogador1 = input('Jogador 1 deve escolher entre Pedra, Papel e Tesoura: ')
    jogador2 = input('Jogador 2 deve escolher entre Pedra, Papel e Tesoura: ')
    if jogador1.lower() == 'papel':
        if jogador2.lower() == 'pedra':
            print('Jogador 1 ganhou a partida!')
        elif jogador2.lower() == 'tesoura':
            print('Jogador 2 ganhou a partida!')
        elif jogador2 == '':
            print('Jogador 2, você não digitou a opção!')
        else:
            print('Empate! jogue novamente!')
    elif jogador1.lower() == 'pedra':
        if jogador2.lower() == 'papel':
            print('Jogador 2 ganhou a partida!')
        elif jogador2.lower() == 'tesoura':
            print('Jogador 1 ganhou a partida!')
        elif jogador2 == '':
            print('Jogador 2, você não digitou a opção!')
        else:
            print('Empate! jogue novamente')
    elif jogador1.lower() == 'tesoura':
        if jogador2.lower() == 'pedra':
            print('Jogador 2 ganhou a partida!')
        elif jogador2.lower() == 'papel':
            print('Jogador 1 ganhou a partida!')
        elif jogador2 == '':
            print('Jogador 2, você não digitou a opção!')
        else:
            print('Empate! jogue novamente')
    elif jogador1 == '':
        if jogador2 == '':
            print('Jogador 1 e 2, vocês não digitaram a opção!')
        else:
            print('Jogador 1, você não digitou a opção!')
    else:
        print('Não entendi o que você digitou!')
    resp = input('Deseja Jogar novamente? ')
else:
    if resp.lower() == 'não':
        print('Obrigado, aguardamos você de volta')
    else:
        print('Não entendi!')
