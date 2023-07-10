armazemnumeros = []
escolha = input('Quer continuar ? [S,N]')
mediarodada = 0
contador = 0
while escolha == 'S':
    mediarodada += 1
    seunumero = int(input('digite seu numero:'))
    armazemnumeros.append(seunumero)
    escolha = input('Quer continuar ? [S,N]')
    contador += 1
if escolha == 'N':
    m = 0
    for i in armazemnumeros:
        if i > m:
            m = i
    l = seunumero
    for i in armazemnumeros:
        if i < l:
            l = i

    valormedia = 0
    for i in armazemnumeros:
        valormedia += i
        mediafinal = valormedia / mediarodada

print('-'*65)
print('O maior valor {} e o menor é {} a media é {} e voce digitou {} numeros'.format(m, l, mediafinal, contador))