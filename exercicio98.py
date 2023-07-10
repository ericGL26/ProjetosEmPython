def contador():
    print('Contagem de 1 em 1')
    minnum = 0
    while minnum < 11:
        print(minnum, end=" ")
        minnum += 1


def contadordois():
    minnum = 0
    while minnum < 11:
        print(minnum, end=" ")
        minnum += 2

contador()
print()
print('-=' * 40)
print('Contagem de 0 a 10 de 2 em 2')
contadordois()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
if passo == 0:
    passo = 1

if fim > inicio:

    def contardortres():
        valor = inicio
        while valor < fim:
            valor += passo
            print(valor)

    contardortres()
else:
    def contardortresre():
        valor = inicio
        while valor > fim:
            valor -= passo
            print(valor)

    contardortresre()