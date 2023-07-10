def ficha():
    nome = input('Digite o nome do jogador: ')
    gols = input(f'Quantos gols {nome} marcou? ')
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato')
ficha()