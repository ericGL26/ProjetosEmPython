lista = {}
listatemp = []
listanum = []
import random
for i in range(0, 4):
    numale = random.randint(0, 6)
    listanum.append(numale)
    listatemp.append([numale])
    lista = listatemp[:]
contador = 0
for i in lista:
    print(f'Jogador {contador} tirou {lista[contador]}')
    contador += 1
print('Ranking dos jogadores:')
listanum.reverse()
c = 1
indice = 0
for i in listanum:
    print(f'{c} lugar jogador{c} tirou {listanum[indice]}')
    indice += 1
    c += 1