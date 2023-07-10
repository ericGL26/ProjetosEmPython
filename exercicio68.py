import random
#parte do bot razadorizador
#parte de escolha do usuario
escolharuser = input('digite sua escolha [I / P]')
numerouser = int(input('digite seu numero'))
#soma
total = bot + numerouser
#parte de verificar se ganhou ou não
while True:
    bot = random.randint(0, 11)
    if escolharuser == 'par':
        if total % 2 == 0:
            print('Voce ganhou')
            break
    else:
        print('voce perdeu')
    if escolharuser == 'inpar':
        if total % 2 != 0:
            print('Voce ganhou')
            break
    else:
            print('Voce perdeu')
print('-' * 60)