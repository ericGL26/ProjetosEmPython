numero1 = int(input('degite um numero'))
numero2 = int(input('degite outro numero'))
numero3 = int(input('degite mais um numero'))

if numero1 > numero2 and numero1 > numero3:
    print('numero {}, é o maior'.format(numero1))
else:
    if numero2 > numero1 and numero2 > numero3:
        print('numero {}, é o maior'.format(numero2))
    else:
        if numero3 > numero2 and numero3 > numero1:
            print('numero {}, é o maior'.format(numero3))