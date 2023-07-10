print('-'*50)
print('LISTAGEM DE PRECO')
print('-'*50)

lista = ('Lapis', 4.42, 'Borracha', 3.31, 'Estojo', 20.00, 'Caderno', 40, 'Cartolina', 7.41)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'{lista[item]:>7.2f}')