lista = []
temporaria = []
nomemenorpeso = ''
nomemaiorpeso = ''
while True:
    suaescolha = input('Quer continuar? [s/n]')
    if suaescolha == 's':
        #PARTE DE ARMAZENAR NA ARRAY LISTA EM FORMA DE ARRAY
        pessoa = input('Digite o nome da pessoa:')
        temporaria.append(pessoa)
        peso = int(input('Digite o peso da pessoa:'))
        temporaria.append(peso)
        lista.append(temporaria[:])
        temporaria.clear()
        #PARTE DA VERIFICACAO MAIOR PESO
        maiorpeso = lista[0][1]
        for i in lista:
            if i[1] > maiorpeso:
                maiorpeso = i[1]
                nomemaiorpeso = i[0]

        menorpeso = 999
        for id in lista:
            if id[1] < menorpeso:
                menorpeso = id[1]
                nomemenorpeso = id[0]
    else:
        break
print('-'*40)
print(f'{len(lista)} pessoas foram cadastradas')
print(f'O maior peso foi de {maiorpeso} do(a) {nomemaiorpeso}')
print(f'O menor peso foi de {menorpeso} do(a) {nomemenorpeso}')
print(lista)