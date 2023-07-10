numero = int(input('degite um numero que deseja'))
listadepares = 0

for i in range(numero + 1):
    if i % 2 == 0:
        listadepares += 1
print('entre 0 e {} existem {} numeros pares'.format(numero, listadepares))