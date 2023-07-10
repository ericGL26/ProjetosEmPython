lista = {"nome": [], "gol": []}
while True:
    golsrodarum = []
    nome = input('Digite seu nome:')
    totpartida = int(input(f'Quantas partidas {nome} jogou? '))
    lista["nome"].append(nome)
    c = 0
    for i in range(0, totpartida):
        c += 1
        golpartida = int(input(f'Quantos gols na {c} partida? '))
        golsrodarum.append(golpartida)
    lista["gol"].append(golsrodarum)
    escolha = input('Quer continuar? [S/N] ')
    print('-' * 40)
    if escolha in 'nN':
        break
print('Jogador ⬇️')
print(f'{lista["nome"]}')
print('Gols ⬇️')
print(f'{lista["gol"]}')
print('Total ⬇️')
totalgols = []
for jogador in lista["gol"]:
    totalgols.append(sum(jogador))
print(totalgols)
c = 0
escolhajogador = int(input('Mostrar dados de qual jogador?'))
if len(lista) < escolhajogador and escolhajogador != 999:
    print(f'jogador {escolhajogador} nao escontrado tente novamente')
if escolhajogador == 999:
    print('Volte sempre')
else:
    print(f'LEVANTAMENTO DE JOGADOR {lista["nome"][escolhajogador]}')
    for i in lista["gol"][escolhajogador]:
        c += 1
        print(f'No jogo {c} fez {i} gols')