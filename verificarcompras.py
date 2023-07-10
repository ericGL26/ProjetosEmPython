print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)
listapreco = []
precototal = 0
maisdemil = 0
escolha = input('Quer continuar? [s \ n')
while escolha == 's':
    escolha = input('Quer continuar? [s \ n')
    if escolha == 's':
        produto = input('Nome do produto:')
        preco = float(input('preço do produto'))
        listapreco.append(preco)
        # parte da verificacao
        precototal += preco
        if preco > 999:
            maisdemil += 1
    else:
        # verificando menor preco
        menornumero = listapreco[0]
        for i in listapreco:
            if i < menornumero:
                menornumero = i
        #printando os resultados
        print('-'*50)
        print(f'O total da compra foi {precototal}')
        print(f'Temos {maisdemil} de mais de R$1000.00')
        print(f'O produto mais barato custa {menornumero}')