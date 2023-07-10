import random
vitorias = 0
while True:
    botn = random.randint(0, 10)
    escolha = input('digite seu escolha')
    numero = int(input('digite seu numero'))
    total = numero + botn
    if escolha == 'par':
        if numero % 2 == 0:
            print('Voce venceu')
            vitorias += 1
        else:
            print('Voce perdeu')
            break
    if escolha == 'inpar':
        if numero % 2 != 0:
            print('Voce venceu')
            vitorias += 1
        else:
            print('Voce perdeu')
            break
print('Voce ganhou {} vitorias consecutivas'.format(vitorias))