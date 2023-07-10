numero1 = int(input('degite um numero'))
numero2 = int(input('degite outro numero'))


if numero1 > numero2:
    print('{} é maior'.format(numero1))
elif numero2 > numero1:
    print('{} é maior'.format(numero2))
elif numero1 == numero2:
    print('nao existe maior os dois sao iguais')