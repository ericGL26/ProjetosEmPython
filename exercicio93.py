lista = {}
nome = input('Digite o nome do jogador:')
partidasvalor = int(input(f'Quantas partidas {nome} jogou?'))
cpartida = 0
valortotagol = 0
golstemp = []
for i in range(0, partidasvalor):
    valorgols = int(input(f'{nome} fez quantos gols na partida {cpartida}?'))
    valortotagol += valorgols
    golstemp.append(valorgols)
    lista["gol"] = golstemp[:]
    cpartida += 1
print('=-'*40)
lista["nome"] = nome
lista["totalgol"] = valortotagol
print(lista)
print('=-'*40)

print(f'O campo nome tem o valor {lista["nome"]}.')
print(f'O campo gol tem o valor {lista["gol"]}.')
print(f'O campo total tem o valor {lista["totalgol"]}.')
print('=-'*40)
c = 0
print(f'O jogador {lista["nome"]} jogou {partidasvalor} partidas')
for i in lista:
    for r in range(0, partidasvalor):
        print(f'Na partida {c}, fez {golstemp[c]}')
        c += 1
    print(f'Foi um total de {lista["totalgol"]} gols!')