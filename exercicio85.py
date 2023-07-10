lista = [[], []]
for i in range(0, 7):
    seunumero = int(input('Digite seu numero'))
    if seunumero % 2 == 0:
        lista[1].append(seunumero)
    else:
        lista[0].append(seunumero)
print('-'*30)
lista[1].sort()
lista[0].sort()
print(f'Os numeros pares da lista são {lista[1]}')
print(f'Os numeros inpares da lista são {lista[0]}')