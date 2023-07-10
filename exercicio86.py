matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
listaverificar = []
listapar = []
valores2linha = matriz[1]
for l in range(0, 3):
    for c in range(0, 3):
        seunumero = int(input('Digite seu numero: '))
        listaverificar.append(seunumero)
        matriz[l][c] = seunumero
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
#parte de verificar numeros pares
for i in listaverificar:
    if i % 2 == 0:
        listapar.append(i)
somatotalpar = 0
for i in listapar:
    somatotalpar += i
print(f'A soma de todos os numeros pares resulta em {somatotalpar}')

soma3coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma da 3 coluna resulta em {soma3coluna}')
maiorvalor2linha = 0
for i in valores2linha:
    if i > maiorvalor2linha:
        maiorvalor2linha = i
print(f'O maior valor da 2 linha é {maiorvalor2linha}')