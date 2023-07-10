escolha = int(input('digite o numero:'))
c = escolha
f = 1
while c > 1:
    c -= 1
    f *= c
    print(c, 'x', end=" ")
print('O fatorial de {} é {}'.format(escolha, f))
