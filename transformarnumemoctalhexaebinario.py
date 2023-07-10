
numero = input('degite um numero')
escolha = input('degite a base de conversao 1 = binario, 2 = octal 3 = hexadecimal')

if escolha == "1":
    numeroint = int(numero)
    numerobin = bin(numeroint)
    print('seu numero em binario é {}'.format(numerobin))
elif escolha == "2":
    numeroint = int(numero)
    numerooct = oct(numeroint)
    print('seu numero em octal é {}'.format(numerooct))
elif  escolha == "3":
    numeroint = int(numero)
    numerohexa = hex(numeroint)
    print('seu numero em octal é {}'.format(numerohexa))