
velocidade = int(input('degite a velocidade do carro'))

if velocidade > 80:
    print('ultrapassou o limite de velocidade multado')
    multavalor = (velocidade - 80 ) * 7
    print('voce foi multado em {}'.format(multavalor))
else:
    print('tudo certo')
