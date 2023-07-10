mediagrupo = 0
idadehomenvelho = 0
nomevelho = ''
totalmulheres = []
v = 0
for p in range(1, 5):
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo: [M,F]')
    mediagrupo += idade
    mediaidade = mediagrupo / 4
    if sexo != 'M' and sexo != 'F':
        print('digite uma genero valido')
        break
        v += 1
    else:
        if p == 1 and sexo == 'M':
            idadehomenvelho = idade
            nomevelho = nome

    if sexo != 'M' and sexo != 'F':
        print('digite um genero valido')
        break
        v += 1
    else:
        if sexo == 'M' and idade > idadehomenvelho:
            idadehomenvelho = idade
            nomevelho = nome
    if sexo != 'M' and sexo != 'F':
        print('digite um genero valido')
        break
        v += 1
    else:
        if sexo == 'F' and idade < 20:
            totalmulheres.append(nome)

if v == 3:
    print('A média de idade do grupo é {}'.format(mediaidade))
    print('O homem mais velho se chama {} e sua idade é de {}'.format(nomevelho, idadehomenvelho))
    print('As mulheres com menos de 20 anos são {}'.format(totalmulheres))
else:
    print('')