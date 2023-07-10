lista = []
while True:
    nota = float(input('Digite a nota:'))
    lista.append(nota)
    escolha = input('Quer continuar? [S/N]')
    if escolha in 'Nn':
        break

def notas():
    """
    Bom voce pode colocar as notas pra
    o codigo mostrar media maior nota menor nota
    situacao e entre outros

    """
    print(f'A quantidade de notas é {len(lista)}')
    #maior nota
    maiornota = lista[0]
    for i in lista:
        if i >= maiornota:
            maiornota = i
    print(f'A maior nota foi {maiornota}')
    #menor nota

    menornota = lista[0]
    for r in lista:
        if r <= menornota:
            menornota = r
    print(f'A menor nota foi {menornota}')
    #media
    tot = 0
    for i in lista:
        tot += i
    media = tot / len(lista)
    print(tot)
    print(f'A media da turma é {media}')

    escolhasit = input('Quer ver a situacao da turma?')
    if escolhasit in 'Ss':
        if media >= 8:
            print('A situacao é Exelente!')
        else:
            if media >= 6 and media < 8:
                print('A situacao é Razoavel')
            else:
                if media < 5:
                    print('A situacao é Horrivel')
print(notas())