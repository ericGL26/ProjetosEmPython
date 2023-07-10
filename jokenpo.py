import random
escolha = input('degite pedra papel ou tesoura ')
lista = ['pedra', 'papel', 'tesoura']
bot = random.choice(lista)
print(bot)
if escolha == 'papel' and bot == 'tesoura':
    print('voce perdeu')
else:
    if escolha == 'tesoura' and bot == 'pedra':
        print('voce perdeu')
    else:
        if escolha == 'tesoura' and bot == 'papel':
            print('voce ganhou')
        else:
          if escolha == 'pedra' and bot == 'papel':
                print('voce perdeu')
            else:
                if escolha == 'papel' and bot == 'pedra':
                    print('voce ganhou')
                else:
                    if escolha == 'pedra' and bot == 'tesoura':
                        print('voce ganhou')