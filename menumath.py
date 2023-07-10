
numero1 = float(input('digite seu numero:'))
numero2 = float(input('digite seu outro numero:'))
print('pressione 1 para somar, 2 para multiplicar, 3 para verificar maior, 4 para adicionar novos numeros e 5 para sair do programa')
escolha = int(input('escolha:'))

if escolha == 1:
    soma = numero1 + numero2
    print('Á soma entre {} e {} resulta em {}'.format(numero1, numero2, soma))
if escolha == 2:
    multiplicar = numero1 * numero2
    print('Á multiplicacao entre {} e {} é {}'.format(numero1, numero2, multiplicar))

if escolha == 3:
    if numero1 > numero2:
        print('o numero {} é o maior'.format(numero1))
    else:
        print('o numero {} é o maior'.format(numero2))

if escolha == 4:
    novonumero1 = int(int(input('digite os novos numeros')))
    novonumero2 = int(int(input('digite os novos numeros')))
    numero1 = novonumero1
    numero2 = novonumero2
    escolha = int(input('escolha:'))

    if escolha == 1:
        soma = numero1 + numero2
        print('Á soma entre {} e {} resulta em {}'.format(numero1, numero2, soma))
    if escolha == 2:
        multiplicar = numero1 * numero2
        print('Á multiplicacao entre {} e {} é {}'.format(numero1, numero2, multiplicar))

    if escolha == 3:
            if numero1 == numero2:
                print('os numeros sao iguais')
            elif numero1 > numero2:
                print('o numero {} é o maior'.format(numero1))
            elif numero2 > numero1:
                print('o numero {} é o maior'.format(numero2))

    if escolha == 5:
        print('')

if escolha == 5:
    print('')
