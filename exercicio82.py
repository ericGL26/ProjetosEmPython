listacompleta = []
listainpar = []
listapar = []
while True:
    escolha = input('Quer continuar? [s / n]')
    if escolha == 's':
        seunumero = int(input('Digite seu numero'))
        listacompleta.append(seunumero)
        if seunumero % 2 == 0:
            listapar.append(seunumero)
        else:
            listainpar.append(seunumero)
    else:
        print('Programa encerrado!!')
        break
print(f'A lista completa é {listacompleta}')
print(f'A lista somente com numeros inpares é {listainpar}')
print(f'A lista somente com numeros pares é {listapar}')