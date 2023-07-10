import random
listanum = []
listapar = []
def sorteio():
    for i in range(0, 5):
        numeroale = random.randint(0, 10)
        listanum.append(numeroale)


def par():
    for i in listanum:
        if i % 2 == 0:
            listapar.append(i)

sorteio()
print(f'Sorteando 5 valores {listanum}')
par()

somapar = 0
for i in listapar:
    somapar += i

print(f'A soma dos valores pares {listanum} resulta em {somapar}')