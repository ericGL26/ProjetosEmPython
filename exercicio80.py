lista = []
for i in range(0, 5):
    seunumero = int(input('Digite seu numero:'))
    if i == 0 or seunumero > lista[-1]:
        lista.append(seunumero)
    else:
        contador = 0
        while contador < len(lista):
            if seunumero <= lista[contador]:
                lista.insert(contador, seunumero)
                break
                contador += 1
print('-'*50)
print(f'A lista em ordem foi {lista} ')