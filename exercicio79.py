listanumero = []
seunumero = int(input('Digite seu numero:'))
listanumero.append(seunumero)
print('numero adicionado com sucesso')
escolha = input('Quer continuar? [s / n]')
while escolha == 's':
        seunumero = int(input('Digite seu numero:'))
        if seunumero in listanumero:
            print('Numero repetido, Não adicionado')
        else:
            listanumero.append(seunumero)
            print('numero adicionado com sucesso')
        escolha = input('Quer continuar? [s / n]')
print(sorted(listanumero))