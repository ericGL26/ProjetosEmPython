lista = [[]]
diclista = {}
idadetotal = 0
listamulher = []
pessoasacimedia = []
while True:
    nome = str(input('Qual seu nome?'))
    idade = int(input('Digite sua idade:'))
    idadetotal += idade
    sexo = input('Sexo: [M/F]')
    escolha = input('Quer continuar?')
    if sexo in 'Ff':
        listamulher.append(nome)

    diclista["nome"] = nome
    diclista["idade"] = idade
    diclista["sexo"] = sexo

    lista.append(diclista.copy())
    diclista.clear()

    media = idadetotal / (len(lista) - 1)
    if idade > media:
        pessoasacimedia.append(nome)
    if escolha in 'sS':
        print('-='*30)
    else:
        break

print(f'{len(lista) - 1} pessoas foram cadastradas')
print(f'A média de idade do grupo é de {media}')
print(f'As mulheres são {listamulher}')
print(f'A lista de pessoas com a idade acima da média é {pessoasacimedia}')