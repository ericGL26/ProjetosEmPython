#calcular preco da viagem

distancia = int(input('degite a distancia da viagem'))

if distancia <= 200:
    preco = distancia * 0.50
else:
    if distancia > 200:
        preco = distancia * 0.45
print('o custo da viagem será {}'.format(preco))