listanumero = []
listapoosicoes = ['Primeira' , 'Segunda', 'Terceira', 'Quarta', 'Quinta']
for i in range(0, 5):
    seunumero = int(input('digite seu numero'))
    listanumero.append(seunumero)
#parte de verficiar MENOR
menornum = listanumero[0]
for c, v in enumerate(listanumero):
    if v <= menornum:
        menornum = v
        posicao = c
        testeposicaomenor = listapoosicoes[posicao]
#parte de verificar MAIOR
maiornum = listanumero[0]
for c, i in enumerate(listanumero):
    if i >= maiornum:
        maiornum = i
        posicaomaior = c
        testeposicao = listapoosicoes[posicaomaior]
print('-'*50)
print(f'A posicao do menor numero foi a {testeposicaomenor} posicao')
print(f'A posicao do maior numero foi a {testeposicao} posicao')
print(f'o menor numero foi {menornum}')
print(f'O maior numero foi {maiornum}')