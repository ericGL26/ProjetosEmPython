listanumero = []
r = 0
listapar = []
pontosdetres = 0
while r < 4:
    r += 1
    escolha = int(input('digite 4 numeros:'))
    listanumero.append(escolha)
quantidadenove = 0
for i in listanumero:
    if i == 3:
        posicaotres = listanumero.index(3)
    if i == 9:
        quantidadenove += 1
    if i % 2 == 0:
        listapar.append(i)
    if i != 3:
        pontosdetres += 1
if pontosdetres == 4:
    print('Nao tem numero 3 nessa lista')
else:
    print('-'*60)
    print(f'O valor 3 está na posicao {posicaotres + 1}')
print(f'O valor 9 apareceu {quantidadenove} vezes')
print(f'Os valores pares sao {listapar}')