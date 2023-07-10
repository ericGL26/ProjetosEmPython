
#Calcular fatorial
numusuario = int(input('Digite seu numero:'))

def fac():
    """
    Programa que calcula fatorial
    e permite q usuario escolha entre ver o calculo ou nao
    """
    total = 1
    for i in range(1, numusuario + 1):
        total *= i
    return total

escolhacal = input('Deseja ver o calculo?:')
if escolhacal in 'Ss':
    for r in range(1, numusuario + 1):
        print(f'{r} x', end=' ')
    print('=')
    print(fac())
if escolhacal in 'Nn':
    resultado = fac()
    print(f'O fatorial é {resultado}')