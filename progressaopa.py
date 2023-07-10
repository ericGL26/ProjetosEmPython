primeiratermo = int(input('primeiro termo:'))
razao = int(input('digite a razao:'))
numeroprint = 0

for r in range(0, 11):
    if r == 0:
        print(primeiratermo, '->')
    else:
        numeroprint += razao
        print(numeroprint, end="->")
        armazenarprint = numeroprint

print('\nVoce deseja mais termos? [S/N]')
escolha = input('Digite sua escolha aqui!')

if escolha == 'S':
    quantidade = int(input('digite quantos termos a mais deseja'))

    if escolha == 'S':
        for r in range(0, quantidade):
            armazenarprint += razao
            print(armazenarprint, end="->")
else:
    print('Codigo encerrado')