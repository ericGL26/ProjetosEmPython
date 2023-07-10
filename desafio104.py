def leiaint():
    ok = False
    while ok != True:
        numerouser = input('Digite um numero:')
        if numerouser.isnumeric():
            print(f'Voce digitou o valor {numerouser}')
            ok = True
            break
        else:
            print('Erro, Digite um numero valido')
leiaint()